import React, { createContext, useContext, useState, useEffect } from "react";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isLoggedInUser, setIsLoggedInUser] = useState(
    localStorage.getItem("isLoggedInUser") === "true"
  );

  useEffect(() => {
    localStorage.setItem("isLoggedInUser", isLoggedInUser);
  }, [isLoggedInUser]);

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
