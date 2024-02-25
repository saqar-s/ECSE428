import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
} from "../Components";
import { FONTS } from "../GLOBAL";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../APIcalls/AccountCalls";
import { Alert, Snackbar } from "@mui/material";

const SignInScreen = () => {
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [emailError, setEmaiError] = React.useState("");
  const [passwordError, setPasswordError] = React.useState("");
  const [error, setError] = React.useState("");
  const [open, setOpen] = React.useState(false);

  const navigate = useNavigate();

  const handleUsernameChange = (text) => {
    setUsername(text);
    setEmaiError("");
  };

  const handlePasswordChange = (text) => {
    setPassword(text);
    setPasswordError("");
  };

  const handleSignUp = () => {
    console.log("Sign Up");
    navigate("/signup");
  };

  const handleLogIn = async () => {
    try {
      const userData = { email: username, password: password };
      const result = await loginUser(userData);

      if (result && result.status === 200) {
        const { name, age } = result.response.data;
        navigate("/account", { state: { username, name, age } });
        console.log(result.message);
      } else if (result.status === 404) {
        setEmaiError(result.message);
      } else if (result.status === 401) {
        setPasswordError(result.message);
      } else {
        setError("Login failed");
        setOpen(true);
      }
    } catch (error) {
      setError("Error loging in:", error.message);
      setOpen(true);
    }
  };

  const handleCLose = (reason) => {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  };

  return (
    <>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          margin: 12,
        }}
      >
        <TitleText text={"Hello!"} />
        <div style={{ marginBottom: "6%" }}>
          <SubTitleText
            text={"Please Sign up or login to get the most out of our website"}
          />
        </div>

        <TextInput
          label={"Username"}
          text={username}
          onClick={handleUsernameChange}
          style={{ marginBottom: 6 }}
          hasError
          helpertext={emailError}
        />
        <TextInput
          label={"Password"}
          text={password}
          onClick={handlePasswordChange}
          style={{ marginBottom: 6 }}
          hasError
          helpertext={passwordError}
          hide
        />

        <CustomButton
          label={"LogIn"}
          onClick={handleLogIn}
          style={{ width: "10%", height: "40px", marginBottom: 6 }}
        />
        <div style={{ fontFamily: FONTS.InriaSerif, fontSize: 16 }}>
          New to Gurment Guru?
        </div>
        <CustomButton
          label={"Sign Up"}
          onClick={handleSignUp}
          style={{ width: "10%", height: "40px", marginTop: 1 }}
        />
      </div>
      <Snackbar open={open} autoHideDuration={3000} onClose={handleCLose}>
        <Alert variant="filled" severity="error" sx={{ width: "100%" }}>
          {error}
        </Alert>
      </Snackbar>
    </>
  );
};

export default SignInScreen;
