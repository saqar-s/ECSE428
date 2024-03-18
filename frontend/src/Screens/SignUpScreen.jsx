import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
} from "../Components";
import { FONTS } from "../GLOBAL";
import { useNavigate } from "react-router-dom";
import { registerUser } from "../APIcalls/AccountCalls";
import { Alert, Snackbar } from "@mui/material";

const SignUpScreen = () => {
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [age, setAge] = React.useState("");
  const [name, setName] = React.useState("");
  const [emailError, setEmailError] = React.useState("");
  const [error, setError] = React.useState("");
  const [open, setOpen] = React.useState(false);

  const navigate = useNavigate();

  const handleUsernameChange = (text) => {
    setUsername(text);
    setEmailError("");
  };

  const handlePasswordChange = (text) => {
    setPassword(text);
  };

  const handleNameChange = (text) => {
    setName(text);
  };

  const handleAgeChange = (text) => {
    setAge(text);
  };

  const handleLogIn = () => {
    navigate("/signin");
  };

  const handleSignUp = async () => {
    try {
      const ageAsInt = parseInt(age);

      if (isNaN(ageAsInt)) {
        console.error("Age must be a valid integer.");
        return;
      }

      const userData = {
        name: name,
        email: username,
        password: password,
        age: ageAsInt,
      };

      const result = await registerUser(userData);

      if (result && result.status === 201) {
        localStorage.setItem("username", username);
        localStorage.setItem("user", name);
        localStorage.setItem("age", age);
        navigate("/account");
      } else if (result.status === 400) {
        setEmailError(result.message);
      } else {
        setError("Registration failed");
        setOpen(true);
      }
    } catch (error) {
      setError("Error signing up:", error.message);
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
          label={"Email (This will be your username)"}
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
        />

        <TextInput
          label={"Name"}
          text={name}
          onClick={handleNameChange}
          style={{ marginBottom: 6 }}
        />
        <TextInput
          label={"Age"}
          text={age}
          onClick={handleAgeChange}
          style={{ marginBottom: 6 }}
        />

        <CustomButton
          label={"Sign Up"}
          onClick={handleSignUp}
          style={{ width: "10%", height: "40px", marginBottom: 6 }}
        />
        <div style={{ fontFamily: FONTS.InriaSerif, fontSize: 16 }}>
          Already have an account?
        </div>
        <CustomButton
          label={"Log In"}
          onClick={handleLogIn}
          style={{
            width: "10%",
            height: "40px",
            marginTop: 1,
            marginBottom: 5,
          }}
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

export default SignUpScreen;
