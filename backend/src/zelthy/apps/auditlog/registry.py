from django.db.models.signals import post_save, pre_save, post_delete
from django.db.models import Model


class AuditLogRegistry:
    def __init__(self, create=True, update=True, delete=True, custom=None):
        from zelthy.apps.auditlog.receivers import log_create, log_update, log_delete

        self._registry = {}
        self._signals = {}

        if create:
            self._signals[post_save] = log_create
        if update:
            self._signals[pre_save] = log_update
        if delete:
            self._signals[post_delete] = log_delete

        if custom is not None:
            self._signals.update(custom)

    def register(
        self, model=None, include_fields=[], exclude_fields=[], mapping_fields={}
    ):
        def registrar(cls):
            if not issubclass(cls, Model):
                raise TypeError("Supplied model is not a valid model")
            self._registry[cls] = {
                "include_fields": include_fields,
                "exclude_fields": exclude_fields,
                "mapping_fields": mapping_fields,
            }
            self._connect_signals(cls)

            # We need to return the class, as the decorator is basically
            # syntactic sugar for:
            # MyClass = auditlog.register(MyClass)
            return cls

        if model is None:
            # If we're being used as a decorator, return a callable with the
            # wrapper.
            return lambda cls: registrar(cls)
        else:
            # Otherwise, just register the model.
            registrar(model)

    def contains(self, model):
        """
        Check if a model is registered with auditlog.

        :param model: The model to check.
        :type model: Model
        :return: Whether the model has been registered.
        :rtype: bool
        """
        return model in self._registry

    def unregister(self, model):
        """
        Unregister a model with auditlog. This will not affect the database.

        :param model: The model to unregister.
        :type model: Model
        """
        try:
            del self._registry[model]
        except KeyError:
            pass
        else:
            self._disconnect_signals(model)

    def _connect_signals(self, model):
        """
        Connect signals for the model.
        """
        for signal in self._signals:
            receiver = self._signals[signal]
            signal.connect(
                receiver, sender=model, dispatch_uid=self._dispatch_uid(signal, model)
            )

    def _disconnect_signals(self, model):
        """
        Disconnect signals for the model.
        """
        for signal, receiver in self._signals.items():
            signal.disconnect(
                sender=model, dispatch_uid=self._dispatch_uid(signal, model)
            )

    def _dispatch_uid(self, signal, model):
        """
        Generate a dispatch_uid.
        """
        return (self.__class__, model, signal)

    def get_model_fields(self, model):
        return {
            "include_fields": self._registry[model]["include_fields"],
            "exclude_fields": self._registry[model]["exclude_fields"],
            "mapping_fields": self._registry[model]["mapping_fields"],
        }


class AuditLogModelRegistry(AuditLogRegistry):
    def __init__(self, *args, **kwargs):
        super(AuditLogModelRegistry, self).__init__(*args, **kwargs)
        raise DeprecationWarning(
            "Use AuditlogModelRegistry instead of AuditLogModelRegistry, AuditLogModelRegistry will be removed in django-auditlog 0.4.0 or later."
        )


auditlog = AuditLogRegistry()
