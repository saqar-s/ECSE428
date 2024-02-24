import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
} from "../Components";

import { useLocation } from "react-router-dom";

const UserAccountScreen = () => {
  const location = useLocation();
  const { username, name, age } = location.state;

  const [usernameModified, setUsername] = React.useState(username);
  const [ageModified, setAge] = React.useState(name);
  const [nameModified, setName] = React.useState(age);

  const handleUsernameChange = (text) => {
    setUsername(text);
  };

  const handleNameChange = (text) => {
    setName(text);
  };

  const handleAgeChange = (text) => {
    setAge(text);
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
      <TitleText text={`Hello ${name}!`} />
      <div style={{ marginBottom: "6%" }}>
        <SubTitleText
          text={"Welcome to your account.You can modify or delete your account"}
        />
      </div>

      <TextInput
        label={"Username"}
        text={usernameModified}
        onClick={handleUsernameChange}
        style={{ marginBottom: 6 }}
      />
      <TextInput
        label={"Name"}
        text={nameModified}
        onClick={handleNameChange}
        style={{ marginBottom: 6 }}
      />
      <TextInput
        label={"Age"}
        text={ageModified}
        onClick={handleAgeChange}
        style={{ marginBottom: 6 }}
      />
      <div
        style={{
          display: "flex",
          flex: 1,
          flexDirection: "row",
          gap: "10%",
          width: "100%",
          justifyContent: "center",
        }}
      >
        <CustomButton label={"Save"} style={{ width: "10%", height: "40px" }} />
        <CustomButton
          label={"Delete Account"}
          style={{ width: "10%", height: "40px" }}
        />
        <CustomButton
          label={"Log out"}
          style={{ width: "10%", height: "40px" }}
        />
      </div>
    </div>
  );
};
export default UserAccountScreen;
