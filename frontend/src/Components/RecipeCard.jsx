import React from "react";
import {
  Card,
  CardHeader,
  CardMedia,
  CardContent,
  CardActions,
  Collapse,
  Typography,
  IconButton,
  Button,
} from "@mui/material";
import FavoriteBorderIcon from "@mui/icons-material/FavoriteBorder";
import FavoriteIcon from "@mui/icons-material/Favorite";
import CustomButton from "./CustomButton";
import { COLORS } from "../GLOBAL";
import { addToFavourites, deleteFavourite } from "../APIcalls/RecipeCalls";
import { useFavorites } from "./FavoritesProvider";
const RecipeCard = ({
  title,
  description,
  author,
  imageURL,
  recipeId,
  deletable,
  handleDelete,
}) => {
  const [showMore, setShowMore] = React.useState(false);
  const { toggleFavorite, isFavorite } = useFavorites();

  const handleShowMore = () => {
    setShowMore(!showMore);
  };

  const handleToggleFavorite = async () => {
    try {
      toggleFavorite(recipeId);
      const username = localStorage.getItem("username");
      const favData = { email: username, id: recipeId };
      if (!isFavorite(recipeId)) {
        await addToFavourites(favData);
      } else {
        await deleteFavourite(favData);
      }
    } catch (error) {
      console.error("Could not add to favourites: ", error);
    }
  };

  //handle add to calendar to be done
  const handleAddToCalendar = () => {
    console.log("add to caledar");
  };

  //handle delete

  const decodedImageURL = `data:image/jpeg;base64,${imageURL}`;
  return (
    <Card
      sx={{
        maxWidth: 300,
        backgroundColor: COLORS.primaryBlue,
        borderRadius: 6,
        borderColor: COLORS.PrimaryPink,
        borderWidth: 2,
        borderStyle: "solid",
      }}
    >
      <CardHeader title={title} subheader={author} />
      <CardMedia
        component="img"
        height="194"
        image={decodedImageURL}
        alt="No image to display"
      />
      <CardContent>
        <Typography
          variant="body2"
          color="text.secondary"
          sx={{
            overflow: "hidden",
            textOverflow: "ellipsis",
            display: "-webkit-box",
            WebkitBoxOrient: "vertical",
            WebkitLineClamp: 2,
          }}
        >
          {description}
        </Typography>
      </CardContent>

      <CardActions
        disableSpacing
        sx={{ display: "flex", flexDirection: "column" }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
            width: "100%",
            justifyContent: "space-between",
          }}
        >
          <CustomButton
            label={"View More"}
            onClick={handleShowMore}
            style={{ width: "40%" }}
          />
          <IconButton onClick={handleToggleFavorite}>
            {isFavorite(recipeId) ? (
              <FavoriteIcon sx={{ fontSize: 30, color: COLORS.Black }} />
            ) : (
              <FavoriteBorderIcon sx={{ fontSize: 30, color: COLORS.Black }} />
            )}
          </IconButton>
        </div>

        <CustomButton
          label={"Add to Calendar"}
          onClick={handleAddToCalendar}
          style={{ width: "100%" }}
        />
        {deletable && (
          <CustomButton
            label={"Delete Recipe"}
            onClick={handleDelete}
            style={{ width: "100%", marginTop: 0.5 }}
          />
        )}
      </CardActions>
    </Card>
  );
};

export default RecipeCard;
