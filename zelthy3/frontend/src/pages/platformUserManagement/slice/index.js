import { createSlice } from '@reduxjs/toolkit';

export const platformUserManagementSlice = createSlice({
	name: 'platformUserManagement',
	initialState: {
		isAddNewUserModalOpen: false,
		isEditUserDetailModalOpen: false,
		isDeactivateUserModalOpen: false,
		rerenderPage: false,
		platformUserManagementData: null,
		platformUserManagementFormData: null,
	},
	reducers: {
		toggleIsAddNewUserModalOpen: (state) => {
			state.isAddNewUserModalOpen = !state.isAddNewUserModalOpen;
		},
		openIsAddNewUserModalOpen: (state, action) => {
			state.isAddNewUserModalOpen = true;
			state.platformUserManagementFormData = action.payload;
		},
		closeIsAddNewUserModalOpen: (state) => {
			state.isAddNewUserModalOpen = false;
			state.platformUserManagementFormData = null;
		},
		toggleIsEditUserDetailModalOpen: (state) => {
			state.isEditUserDetailModalOpen = !state.isEditUserDetailModalOpen;
		},
		openIsEditUserDetailModalOpen: (state, action) => {
			state.isEditUserDetailModalOpen = true;
			state.platformUserManagementFormData = action.payload;
		},
		closeIsEditUserDetailModalOpen: (state) => {
			state.isEditUserDetailModalOpen = false;
			state.platformUserManagementFormData = null;
		},
		toggleIsDeactivateUserModalOpen: (state) => {
			state.isDeactivateUserModalOpen += !state.isDeactivateUserModalOpen;
		},
		openIsDeactivateUserModalOpen: (state, action) => {
			state.isDeactivateUserModalOpen = true;
			state.platformUserManagementFormData = action.payload;
		},
		closeIsDeactivateUserModalOpen: (state) => {
			state.isDeactivateUserModalOpen = false;
			state.platformUserManagementFormData = null;
		},
		setPlatformUserManagementData: (state, action) => {
			state.platformUserManagementData = action.payload;
		},
		toggleRerenderPage: (state) => {
			state.rerenderPage = !state.rerenderPage;
		},
	},
});

export const {
	toggleIsAddNewUserModalOpen,
	openIsAddNewUserModalOpen,
	closeIsAddNewUserModalOpen,
	toggleIsEditUserDetailModalOpen,
	openIsEditUserDetailModalOpen,
	closeIsEditUserDetailModalOpen,
	toggleIsDeactivateUserModalOpen,
	openIsDeactivateUserModalOpen,
	closeIsDeactivateUserModalOpen,
	setPlatformUserManagementData,
	toggleRerenderPage,
} = platformUserManagementSlice.actions;

export const selectIsAddNewUserModalOpen = (state) =>
	state.platformUserManagement.isAddNewUserModalOpen;

export const selectIsEditUserDetailModalOpen = (state) =>
	state.platformUserManagement.isEditUserDetailModalOpen;

export const selectIsDeactivateUserModalOpen = (state) =>
	state.platformUserManagement.isDeactivateUserModalOpen;

export const selectRerenderPage = (state) =>
	state.platformUserManagement.rerenderPage;

export const selectPlatformUserManagementData = (state) =>
	state.platformUserManagement.platformUserManagementData;

export const selectPlatformUserManagementFormData = (state) =>
	state.platformUserManagement.platformUserManagementFormData;

export default platformUserManagementSlice.reducer;
