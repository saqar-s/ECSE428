import React from "react";
import {
  TitleText,
  SubTitleText,
  LargeTextInputWhite,
  TextInput,
  CustomButton,
} from "../Components";
import { COLORS, FONTS } from "../GLOBAL";
import { useNavigate } from "react-router-dom";
import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogActions,
  DialogContentText,
  Typography,
  colors,
  Alert,
  Snackbar
} from "@mui/material";
import { createRecipe } from "../APIcalls/RecipeCalls";

const PostScreen = () => {
  const [dialogOpen, setDialogOpen] = React.useState(false);
  const [recipeName, setRecipeName] = React.useState("");
  const [ingredients, setIngredients] = React.useState("");
  const [description, setDescription] = React.useState("");
  // const [passwordError, setPasswordError] = React.useState("");
  const [error, setError] = React.useState("");
  const [open, setOpen] = React.useState(false);


  const handleRecipeNameChange = (text) => {
    setRecipeName(text);
  };
  const handleIngredientsChange = (text) => {
    setIngredients(text);
  };
  const handleDescriptionChange = (text) => {
    setDescription(text);
  };
  const handleCreateRecipe = async () => {
    try {
      const userData = {
        name: recipeName,
        ingredients: ingredients,
        description: description,
        email: localStorage.get("username")
      };

      const result = await createRecipe(userData);
      console.log(result)
      console.log(ingredients)

      if (result && result.status === 200) {
        setRecipeName("");
        setIngredients("");
        setDescription("");
        // setError("createdRecipe")
      } else if (result.status === 400) {
        // setError(result.message);
      } else {
        // setError("Registration failed");
        // setOpen(true);
        
      }
    } catch (error) {
      // setError("Error creating recipe:", error.message);
      // setOpen(true);
    }


  };

  const handleCLose = (reason) => {
    if (reason === "clickaway") {
      return;
    }
    setOpen(false);
  };

  const handleModalClick = () => {
    setDialogOpen(!dialogOpen);
    console.log();
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
      <TitleText text={"Welcome to Gourmet Guru!"} />
      <div style={{ marginBottom: "6%" }}>
        <SubTitleText text={"Make a post and share it with others to enjoy!"} />
      </div>
      <CustomButton
        label={"Make a post"}
        style={{ width: "30%" }}
        onClick={handleModalClick}
      />
      {dialogOpen && (
        <Dialog
          open={dialogOpen}
          onClose={handleModalClick}
          aria-labelledby="scroll-dialog-title"
          aria-describedby="scroll-dialog-description"
          PaperProps={{
            sx: {
              borderRadius: 12,
              backgroundColor: COLORS.PrimaryPink,
              width: "70%",
            },
          }}
        >
          <DialogTitle
            id="scroll-dialog-title"
            alignSelf={"center"}
            sx={{
              fontFamily: FONTS.InriaSerif,
              fontSize: "1.5vw",
              fontWeight: "2.5vw",
              color: COLORS.White,
            }}
          >
            Create your post
          </DialogTitle>
          <DialogContent dividers>
            
            <TextInput
              label={"Choose a picture for your post"}
              width={"100%"}
              style={{ marginBottom: 2 }}
              labelColor="white"
            />
            <TextInput
              label={"What is the name/title of your recipe?"}
              width={"100%"}
              style={{ marginBottom: 2 }}
              labelColor="white"
              text={recipeName}
              onClick={handleRecipeNameChange}
            />
            <TextInput
              label={
                "What are the ingredients of your recipe? Separate each ingrediant with a comma(e.g: milk, ground beef, etc)"
              }
              width={"100%"}
              style={{ marginBottom: 2 }}
              labelColor="white"
              text={ingredients}
              onClick={handleIngredientsChange}
            />
            <TextInput
              label={"Write the instructions to your recipe."}
              width={"100%"}
              isMultiline={true}
              style={{ marginBottom: 2 }}
              labelColor="white"
              text={description}
              onClick={handleDescriptionChange}
            />
            <div style={{ display: "flex", justifyContent: "center" }}>
              <CustomButton
                label={"Save"}
                onClick={handleCreateRecipe}
                style={{ width: "20%", height: "50px" }}
                backgroundChangeColor="white"
                backgroundColor={COLORS.primaryBlue}
              />
            </div>
          </DialogContent>
        </Dialog>
      )}
      <Snackbar open={open} autoHideDuration={3000} onClose={handleCLose}>
      <Alert variant="filled" severity="danger" sx={{ width: "100%" }}>
        {error} 
      </Alert>
    </Snackbar>
    </div>
  );
};
export default PostScreen;
