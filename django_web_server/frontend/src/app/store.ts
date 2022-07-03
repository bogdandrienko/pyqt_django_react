import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import { combineReducers } from "redux";
import counterReducer from '../features/counter/counterSlice';
import {ImageReducer} from '../pages/HomePage'
import thunk from "redux-thunk";

const globalReducer = combineReducers({
  counter: counterReducer,
  ImageStore: ImageReducer,
});

const initialState = {
};

export const store = configureStore({
  reducer: globalReducer,
  devTools: true,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
  preloadedState: initialState,
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
