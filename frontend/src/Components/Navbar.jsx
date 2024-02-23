import React from "react";
import {
  AppBar,
  Toolbar,
  Button,
  ThemeProvider,
  createTheme,
} from "@mui/material";
import { COLORS, FONTS } from "../GLOBAL";
import { Link } from "react-router-dom";

const NavBar = () => {
  const pages = [
    { name: "Dashboard", path: "/" },
    { name: "Make a post", path: "/post" },
    { name: "Calendar", path: "/calendar" },
    { name: "Favorites", path: "/favorites" },
    { name: "Account", path: "/signin" },
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
      fontSize: 18,
      fontWeightMedium: "normal",
    },
  });

  return (
    <ThemeProvider theme={theme}>
      <AppBar position="static" sx={styles.appBar}>
        <Toolbar sx={styles.toolbar}>
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
    justifyContent: "center",
    gap: 4,
    overflowX: "auto",
    overflowY: "hidden",
    maxHeight: 100,
    whiteSpace: "nowrap",
  },
  button: {
    textTransform: "none",
  },
};

export default NavBar;
