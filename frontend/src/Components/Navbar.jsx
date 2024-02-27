import React from "react";
import {
  AppBar,
  Toolbar,
  Button,
  ThemeProvider,
  createTheme,
  Avatar,
} from "@mui/material";
import { COLORS, FONTS } from "../GLOBAL";
import { Link } from "react-router-dom";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import { useHistory } from "react-router-dom";

const NavBar = () => {
  const pages = [
    { name: "Dashboard", path: "/" },
    { name: "Make a post", path: "/post" },
    { name: "Calendar", path: "/calendar" },
    { name: "Favorites", path: "/favorites" },
  ];

  const theme = createTheme({
    palette: {
      primary: {
        main: COLORS.Beige,
        contrastText: COLORS.Black,
      },
    },
    typography: {
      fontFamily: FONTS.InriaSerif,
      fontSize: 20,
      fontWeightMedium: "normal",
    },
  });

  const handleAccountClick = () => {
    const loggedInUser = localStorage.getItem("username");
    let result;
    if (loggedInUser !== null) {
      result = "/account";
    } else {
      result = "/signin";
    }
    return result;
  };
  const accountPath = handleAccountClick();
  return (
    <ThemeProvider theme={theme}>
      <AppBar position="static" sx={styles.appBar}>
        <Toolbar sx={styles.toolbar}>
          <div style={styles.centerButtons}>
            {pages.map((page) => (
              <Button
                key={page.name}
                color="inherit"
                sx={styles.button}
                component={Link}
                to={page.path}
              >
                {page.name}
              </Button>
            ))}
          </div>
          <div style={styles.accountButton}>
            <Button
              color="inherit"
              sx={styles.button}
              component={Link}
              to={accountPath}
              endIcon={
                <Avatar sx={styles.avatarIcon}>
                  <AccountCircleIcon />
                </Avatar>
              }
            >
              Account
            </Button>
          </div>
        </Toolbar>
      </AppBar>
    </ThemeProvider>
  );
};

const styles = {
  appBar: {
    bgcolor: "main",
  },
  toolbar: {
    display: "flex",
    justifyContent: "center",
    overflowX: "auto",
    overflowY: "hidden",
    maxHeight: 100,
    whiteSpace: "nowrap",
    alignItems: "center",
  },
  centerButtons: {
    display: "flex",
    gap: 24,
  },
  accountButton: {
    position: "absolute",
    right: "55px",
  },
  button: {
    textTransform: "none",
  },
  avatarIcon: {
    width: 30,
    height: 30,
  },
};

export default NavBar;
