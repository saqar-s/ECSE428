import React from "react";
import {
  TitleText,
  SubTitleText,
  LargeTextInputWhite,
  TextInput,
  FileInput,
  CustomButton,
  RecipeCard,
} from "../Components";
import { COLORS, FONTS } from "../GLOBAL";
import { useNavigate } from "react-router-dom";
import {
  Dialog,
  DialogContent,
  DialogTitle,
  Alert,
  Snackbar,
  Grid,
} from "@mui/material";
import {
  createRecipe,
  getRecipes,
  deleteRecipe,
} from "../APIcalls/RecipeCalls";
import { useAuth } from "../AuthContext";

const PostScreen = () => {
  const [dialogOpen, setDialogOpen] = React.useState(false);
  const [recipeName, setRecipeName] = React.useState("");
  const [ingredients, setIngredients] = React.useState("");
  const [description, setDescription] = React.useState("");
  const [error, setError] = React.useState("");
  const [open, setOpen] = React.useState(false);
  const [selectedFile, setSelectedFile] = React.useState(null);
  const [recipes, setRecipes] = React.useState([]);

  const email = localStorage.getItem("username");
  const { isLoggedInUser } = useAuth();

  React.useEffect(() => {
    getRecipes(email)
      .then((response) => {
        console.log(response.data.recipes);
        setRecipes(response.data.recipes);
      })
      .catch((error) => {
        console.error("Error fetching recipes:", error);
      });
  }, [recipes, email]);
  const cardsPerRow = Math.min(4, recipes.length);

  const handleFileSelect = (file) => {
    setSelectedFile(file);
  };

  const handleRecipeNameChange = (text) => {
    setRecipeName(text);
  };
  const handleIngredientsChange = (text) => {
    setIngredients(text);
  };
  const handleDescriptionChange = (text) => {
    setDescription(text);
  };

  const readFileAsBase64 = async (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => {
        resolve(reader.result.split(",")[1]);
      };
      reader.onerror = (error) => reject(error);
      reader.readAsDataURL(file);
    });
  };

  const handleCreateRecipe = async () => {
    try {
      const imageFile = selectedFile;
      let imageData = null;

      if (imageFile) {
        imageData = await readFileAsBase64(imageFile);
        console.log(imageData);
      }

      const userData = {
        name: recipeName,
        ingredients: ingredients,
        description: description,
        email: email,
        image: imageData,
      };

      const result = await createRecipe(userData);
      setDialogOpen(false);
      if (result && result.status === 201) {
        setRecipeName("");
        setIngredients("");
        setDescription("");
        setSelectedFile(null);
      } else if (result.status === 400) {
        setError(result.message);
        console.log(result.message);
      } else {
        setError("failed");
        console.log("failed to create recipe");
      }
    } catch (error) {
      setError("Error creating recipe:", error.message);
      console.log(error);
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

  const handleDelete = async (recipeId) => {
    try {
      const response = await deleteRecipe({ id: recipeId });
      if (response && response.status === 200) {
        console.log("Successfully deleted");
        getRecipes(email)
          .then((response) => {
            console.log(response.data.recipes);
            setRecipes(response.data.recipes);
          })
          .catch((error) => {
            console.error("Error fetching recipes:", error);
          });
      }
    } catch (error) {
      console.error("Error deleting recipe:", error);
    }
  };

  return isLoggedInUser ? (
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
      <Grid container spacing={2} marginLeft={2}>
        {recipes.map((recipe, index) => (
          <Grid item xs={12 / cardsPerRow} key={index}>
            <RecipeCard
              title={recipe.name}
              imageURL={recipe.image}
              description={recipe.description}
              author={recipe.email}
              recipeId={recipe.id}
              deletable={true}
              handleDelete={() => handleDelete(recipe.id)}
            />
          </Grid>
        ))}
      </Grid>
      <CustomButton
        label={"Create a new post"}
        style={{ width: "30%", marginTop: 6 }}
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
            <FileInput
              label={"Choose a picture for your post"}
              width={"100%"}
              style={{ marginBottom: 2 }}
              labelColor="white"
              onFileSelect={handleFileSelect}
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
                label={"Create Post"}
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
        <Alert variant="filled" severity="error" sx={{ width: "100%" }}>
          {error}
        </Alert>
      </Snackbar>
    </div>
  ) : (
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
      <div>
        You need to be logged in to be able to post and view your created
        recipes
      </div>
    </div>
  );
};
export default PostScreen;
