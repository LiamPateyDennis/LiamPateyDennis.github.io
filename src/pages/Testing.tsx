import ProcessImage from "../components/ProcessImage";
import Upload from "../components/Upload";
import Box from "@mui/material/Box";
import box from "../types/box";
import { ThemeProvider } from "@mui/material";
import theme from "../types/theme";
import Grid from "@mui/material/Grid";
import BlackWhiteImage from "../components/BlackWhiteImage";
import React from "react";
import Repetition from "./Repetition";
import FuncRepetition from "../components/FuncRepetition";

function Testing() {
  const [imageSrc, setImageSrc] = React.useState<string | null>(null);
  const [invertedSrc, setInvertedSrc] = React.useState<string | null>(null);

  return (
    <ThemeProvider theme={theme}>
      <Grid display="flex" justifyContent="center" alignItems="center">
        <Box sx={box}>
          <Upload onUpload={(src: string) => setImageSrc(src)} />

          {imageSrc && (
            <BlackWhiteImage
              src={imageSrc}
              onCanvas={(canvas) => {
                try {
                  const out = FuncRepetition(canvas);
                  setInvertedSrc(out.toDataURL());
                } catch (e) {
                  setInvertedSrc(null);
                }
              }}
            />
          )}

          {invertedSrc && (
            <Box sx={{ marginTop: 2 }}>
              <img
                src={invertedSrc}
                alt="inverted"
                style={{ maxWidth: "100%" }}
              />
            </Box>
          )}
        </Box>
      </Grid>
    </ThemeProvider>
  );
}

export default Testing;
