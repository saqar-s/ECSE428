import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
} from "../Components";
import { FONTS } from "../GLOBAL";
import { useNavigate } from "react-router-dom";

const SignInScreen = () => {
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  const navigate = useNavigate();

  const handleUsernameChange = (text) => {
    setUsername(text);
  };

  const handlePasswordChange = (text) => {
    setPassword(text);
  };

  const handleLogIn = () => {
    console.log("LogedIn");
  };

  const handleSignUp = () => {
    console.log("Sign Up");
    navigate("/signup");
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        margin: 12,
      }}
    >
      <TitleText text={"Hello!"} />
      <div style={{ marginBottom: "10%" }}>
        <SubTitleText
          text={"Please Sign up or login to get the most out of our website"}
        />
      </div>

      <TextInput
        label={"Username"}
        text={username}
        onClick={handleUsernameChange}
        style={{ marginBottom: 6 }}
      />
      <TextInput
        label={"Password"}
        text={password}
        onClick={handlePasswordChange}
        style={{ marginBottom: 6 }}
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
  );
};

export default SignInScreen;
