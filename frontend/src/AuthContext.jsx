import React, { createContext, useContext, useState } from "react";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isLoggedInUser, setIsLoggedInUser] = useState(false);
  console.log(isLoggedInUser);

  const login = () => {
    setIsLoggedInUser(true);
  };

  const logout = () => {
    setIsLoggedInUser(false);
  };
  return (
    <AuthContext.Provider
      value={{ isLoggedInUser, setIsLoggedInUser, login, logout }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
