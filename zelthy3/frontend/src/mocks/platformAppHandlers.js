import { rest } from 'msw';
import moment from 'moment';

const appsMockData = [
	{
		id: 3,
		schema_name: 'App01',
		created_at: '2023-09-04T04:10:12.168551Z',
		created_by: '',
		modified_at: '2023-09-05T04:10:12.168566Z',
		modified_by: '',
		uuid: '953d129d-1c2c-4478-9f08-bcafbfafb301',
		name: 'App01',
		description: 'App01 Tenant',
		tenant_type: 'shared',
		status: 'staged',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
	{
		id: 5,
		schema_name: 'App02',
		created_at: '2023-01-24T09:17:32.739628Z',
		created_by: '',
		modified_at: '2023-04-24T09:17:32.739661Z',
		modified_by: '',
		uuid: '8e70a30b-0607-4c5b-9268-f6f0df720d7d',
		name: 'App02',
		description: 'This is my tenth app',
		tenant_type: 'app',
		status: 'deployed',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
	{
		id: 6,
		schema_name: 'App03',
		created_at: '2023-08-24T09:24:01.996087Z',
		created_by: '',
		modified_at: '2023-08-24T09:24:01.996122Z',
		modified_by: '',
		uuid: '92887414-1a7a-4a45-8cd3-86f076936cc8',
		name: 'App03',
		description: 'This is my tenth app',
		tenant_type: 'app',
		status: 'deployed',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
	{
		id: 7,
		schema_name: 'App04',
		created_at: '2023-08-24T09:29:47.296933Z',
		created_by: '',
		modified_at: '2023-08-24T09:29:47.296973Z',
		modified_by: '',
		uuid: '4d427afd-fc48-4f3e-b84d-d7d5cbb22505',
		name: 'App04',
		description: 'This is my tenth app',
		tenant_type: 'app',
		status: 'deployed',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
	{
		id: 9,
		schema_name: 'zprj1app1',
		created_at: '2023-08-27T21:22:54.186690Z',
		created_by: '',
		modified_at: '2023-08-27T21:22:54.186704Z',
		modified_by: '',
		uuid: 'a05ae8c0-8e33-4018-aa49-900a2403e5cb',
		name: 'zprj1app1',
		description: 'This is my tenth app',
		tenant_type: 'app',
		status: 'deployed',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
	{
		id: 10,
		schema_name: 'zprj1app2',
		created_at: '2023-08-27T21:25:10.298465Z',
		created_by: '',
		modified_at: '2023-08-27T21:25:10.298495Z',
		modified_by: '',
		uuid: 'a596233f-59fc-49df-a257-0d5e60126bde',
		name: 'zprj1app2',
		description: 'This is my tenth app',
		tenant_type: 'app',
		status: 'deployed',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
	{
		id: 11,
		schema_name: 'zprj1app3',
		created_at: '2023-08-27T21:26:29.584801Z',
		created_by: '',
		modified_at: '2023-08-27T21:26:29.584855Z',
		modified_by: '',
		uuid: '3b8d7f45-fe7c-45d7-8aad-7c8f848c75f9',
		name: 'zprj1app3',
		description: 'This is my tenth app',
		tenant_type: 'app',
		status: 'deployed',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
	{
		id: 12,
		schema_name: 'zprj1app4',
		created_at: '2023-08-27T21:30:07.519559Z',
		created_by: '',
		modified_at: '2023-08-27T21:30:07.519585Z',
		modified_by: '',
		uuid: 'c14061da-6061-4537-be05-46c57f4a8a94',
		name: 'zprj1app4',
		description: 'This is my tenth app',
		tenant_type: 'app',
		status: 'deployed',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
	{
		id: 13,
		schema_name: 'zprj1app5',
		created_at: '2023-08-27T21:33:38.871839Z',
		created_by: '',
		modified_at: '2023-08-27T21:33:38.871873Z',
		modified_by: '',
		uuid: '03d6180d-1f67-430b-b8ea-473a6647349d',
		name: 'zprj1app5',
		description: 'This is my tenth app',
		tenant_type: 'app',
		status: 'deployed',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
	{
		id: 14,
		schema_name: 'zprj1app6',
		created_at: '2023-08-27T21:34:17.297128Z',
		created_by: '',
		modified_at: '2023-08-27T21:34:18.435520Z',
		modified_by: '',
		uuid: '288ddf7d-9d8c-406c-8148-419d6b824fa7',
		name: 'zprj1app6',
		description: 'This is my tenth app',
		tenant_type: 'app',
		status: 'deployed',
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
		domain_url: 'https://test.zelthy.com',
	},
];

export const platformAppHandlers = [
	rest.post('/api/v1/apps/', (req, res, ctx) => {
		let { name, description } = req.body;

		appsMockData.unshift({
			id: 14,
			schema_name: 'zprj1app6',
			created_at: moment(),
			created_by: '',
			modified_at: moment(),
			modified_by: '',
			uuid: moment().toString(),
			name: name,
			description: description,
			tenant_type: 'app',
			status: 'staged',
			deployed_on: null,
			suspended_on: null,
			deleted_on: null,
			timezone: null,
			language: null,
			date_format: null,
			datetime_format: null,
			logo: null,
			extra_config: null,
			domain_url: 'https://test.zelthy.com',
		});

		return res(
			ctx.delay(500),
			// Success
			ctx.status(200),
			ctx.json({
				success: true,
				response: {
					app_uuid: '6aadc375-75cc-4a74-b6d3-e421b063afb4',
					message: 'App Launch Initiated Successfully',
				},
			})

			// Fail
			// ctx.status(400),
			// ctx.json({
			// 	success: false,
			// 	response: {
			// 		message: 'App name already taken',
			// 	},
			// })
		);
	}),

	rest.get('/api/v1/apps/', (req, res, ctx) => {
		return res(
			ctx.delay(500),
			ctx.status(200),
			ctx.json({
				success: true,
				response: {
					apps: appsMockData,
					message: 'All apps fetched successfully',
				},
			})
		);
	}),
];