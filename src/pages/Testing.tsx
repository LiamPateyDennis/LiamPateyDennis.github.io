import ProcessImage from "../components/ProcessImage";
import Upload from "../components/Upload";
import Box from "@mui/material/Box";
import box from "../types/box";
import { ThemeProvider } from "@mui/material";
import theme from "../types/theme";
import Grid from "@mui/material/Grid";
import BlackWhiteImage from "../components/BlackWhiteImage";
import React from "react";
import EncodeRepetition from "../components/repetition/EncodeRepetition";
import GenerateNoise from "../components/GenerateNoise";
import ConvertToBinary from "../components/ConvertToBinary";

function Testing() {
  const [imageSrc, setImageSrc] = React.useState<string | null>(null);
  const [repetitionSrc, setRepetitionSrc] = React.useState<string | null>(null);
  const [noiseSrc, setNoiseSrc] = React.useState<string | null>(null);

  let encoded: HTMLCanvasElement | null = null;

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
                  encoded = EncodeRepetition(canvas);
                  setRepetitionSrc(encoded.toDataURL());
                } catch (e) {
                  setRepetitionSrc(null);
                }
                try {
                  const outNoise = GenerateNoise(encoded, 0.005);
                  setNoiseSrc(outNoise.toDataURL());
                } catch (e) {
                  setNoiseSrc(null);
                }
              }}
            />
          )}
          {/* {imageSrc && (
            <ConvertToBinary
              src={imageSrc}
              onCanvas={(canvas) => {
                try {
                  const out = EncodeRepetition(canvas);
                  setRepetitionSrc(out.toDataURL());
                } catch (e) {
                  setRepetitionSrc(null);
                }
              }}
            />
          )} */}

          {repetitionSrc && (
            <Box sx={{ marginTop: 2 }}>
              <img
                src={repetitionSrc}
                alt="inverted"
                style={{ maxWidth: "100%" }}
              />
            </Box>
          )}
          {noiseSrc && (
            <Box sx={{ marginTop: 2 }}>
              <img src={noiseSrc} alt="inverted" style={{ maxWidth: "100%" }} />
            </Box>
          )}
        </Box>
      </Grid>
    </ThemeProvider>
  );
}

export default Testing;
