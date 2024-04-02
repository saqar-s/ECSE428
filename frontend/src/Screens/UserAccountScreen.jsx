import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
} from "../Components";
import {
  modifyUserDetails,
  logoutUser,
  deleteUser,
} from "../APIcalls/AccountCalls";
import { useNavigate } from "react-router-dom";
import {
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Button,
} from "@mui/material";
import { useAuth } from "../AuthContext";

const UserAccountScreen = () => {
  const navigate = useNavigate();
  const username = localStorage.getItem("username");
  const name = localStorage.getItem("user");
  const age = localStorage.getItem("age");

  const [usernameModified, setUsername] = React.useState(username);
  const [ageModified, setAge] = React.useState(age);
  const [nameModified, setName] = React.useState(name);
  const [open, setOpen] = React.useState(false);
  const [deleteError, setDeleteError] = React.useState("");

  const handleUsernameChange = (text) => {
    setUsername(text);
  };

  const handleNameChange = (text) => {
    setName(text);
  };

  const handleAgeChange = (text) => {
    setAge(text);
  };

  const handleModify = async () => {
    try {
      const response = await modifyUserDetails({
        name: nameModified,
        age: ageModified,
        email: username,
      });
      if (response && response.status === 200) {
        console.log("Changing info to: ", nameModified, ageModified);
        console.log("From: ", name, age);
      }
    } catch (error) {
      console.error("Could not modify data: ", error);
    }
  };
  const { logout } = useAuth();
  const handleLogout = async () => {
    try {
      const response = await logoutUser();

      logout();
      localStorage.clear();
    } catch (error) {
      console.error("Could not logout: ", error);
    }
    navigate("/signin");
  };

  const handleDialog = () => {
    setOpen(!open);
  };

  const handleDeleteAccount = async () => {
    try {
      const response = await deleteUser(username);
      if (response && response.status === 200) {
        setOpen(!open);
        logout();
        localStorage.clear();
        navigate("/signin");
      }
    } catch (error) {
      console.error("Could not delete: ", error);
      setDeleteError("Could not delete your account");
    }
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

      <span style={{ color: "red" }}> You cannot modify your email</span>
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
        <CustomButton
          label={"Save"}
          style={{ width: "10%", height: "40px" }}
          onClick={handleModify}
        />
        <CustomButton
          label={"Delete Account"}
          style={{ width: "10%", height: "40px" }}
          onClick={handleDialog}
        />
        {open && (
          <Dialog
            open={open}
            onClose={handleDialog}
            aria-labelledby="alert-dialog-title"
            aria-describedby="alert-dialog-description"
          >
            <DialogTitle id="alert-dialog-title">
              {"Are you sure you want to delete your account?"}
            </DialogTitle>
            <DialogContent>
              <DialogContentText id="alert-dialog-description">
                Once you delete your account you cannot revert the change and
                will need to create a new account if you would like to use our
                website.
              </DialogContentText>
            </DialogContent>
            <DialogActions>
              <Button onClick={handleDialog}>Cancel</Button>
              <Button onClick={handleDeleteAccount} autoFocus>
                Ok
              </Button>
            </DialogActions>
          </Dialog>
        )}
        <CustomButton
          label={"Log out"}
          style={{ width: "10%", height: "40px" }}
          onClick={handleLogout}
        />
      </div>
    </div>
  );
};
export default UserAccountScreen;
