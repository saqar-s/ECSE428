import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Navbar } from "./Components";
import {
  SignInScreen,
  SignUpScreen,
  DashboardScreen,
  UserAccountScreen,
  PostScreen,
  FavoritesScreen
} from "./Screens";
import UserListScreen from "./Screens/UserListScreen";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<DashboardScreen />} />
        <Route path="/signin" element={<SignInScreen />} />
        <Route path="/signup" element={<SignUpScreen />} />
        <Route path="/account" element={<UserAccountScreen />} />
        <Route path="/post" element={<PostScreen />} />
        <Route path="/favourites" element={<FavoritesScreen />} />
        <Route path="/userlist" element={<UserListScreen />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
