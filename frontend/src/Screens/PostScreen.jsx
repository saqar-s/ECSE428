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
import { deleteRecipe } from "../APIcalls/RecipeCalls";

const PostScreen = () => {
  const [dialogOpen, setDialogOpen] = React.useState(false);
  const [recipeName, setRecipeName] = React.useState("");
  const [ingredients, setIngredients] = React.useState("");
  const [description, setDescription] = React.useState("");
  // const [passwordError, setPasswordError] = React.useState("");
  const [error, setError] = React.useState("");
  const [open, setOpen] = React.useState(false);
  const [recipeNameToDelete, setRecipeNameToDelete] = React.useState("");


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
    console.log(localStorage.getItem("username"))
    try {
      const userData = {
        name: recipeName,
        ingredients: ingredients,
        description: description,
        email: localStorage.getItem("username"),
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
  }

  const handleNameForDelete = (text) => {
    setRecipeNameToDelete(text);
  };

  const handleDeleteRecipe = async () => {
    try {
      const userData = {
        name : recipeNameToDelete,
      };
  
      const result = await deleteRecipe(userData);
      console.log(`this is what result is giving me ${result} and the status is ${result.status}`);
      if (result && result.status === 200) {
        recipeNameToDelete("");
      }
      else {
        console.log(`something bad is hapenning bobby ${recipeNameToDelete}`)
      }
    }
    catch (error) {

    }
  }

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
        style={{ width: "30%", marginBottom: 6 }}
        onClick={handleModalClick}
      />
      <TextInput
          label={"Delete a Recipe"}
          text={recipeNameToDelete}
          onClick={handleNameForDelete}
          style={{ marginBottom: 6 }}
        />
        <CustomButton
          label={"Delete Recipe"}
          onClick={handleDeleteRecipe}
          style={{ width: "10%", height: "40px", marginBottom: 6 }}
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
