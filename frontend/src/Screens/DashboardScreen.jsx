import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
  RecipeCard,
} from "../Components";
import { Grid } from "@mui/material";
const DashboardScreen = () => {
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
      <Grid container spacing={2}>
        <Grid item xs={3}>
          <RecipeCard
            title={"something"}
            imageURL="../pasta.jpeg"
            description={
              "n hfgiubgf ivfhuihfowb krfhiwp; wsuhrow  hfd dfb dufgkurfbl shbfiofh dfbol kwfhuwhuil hubfuiebfohnesofiheirubf"
            }
            author={"Saghar"}
          ></RecipeCard>
        </Grid>
        <Grid item xs={3}>
          <RecipeCard
            title={"something"}
            imageURL="../pasta.jpeg"
            description={
              "n hfgiubgf ivfhuihfowb krfhiwp; wsuhrow kwfhuwhuil hubfuiebfohnesofiheirubf"
            }
            author={"Saghar"}
          ></RecipeCard>{" "}
        </Grid>
      </Grid>
    </div>
  );
};

export default DashboardScreen;
