import Box from "@mui/material/Box";
import theme from "../types/theme";
import { ThemeProvider } from "@mui/material";
import Grid from "@mui/material/Grid";
import text from "../types/text";
import box from "../types/box";
import heading from "../types/heading";
import { MathJaxContext, MathJax } from "better-react-mathjax";
import config from "../types/configMath";
import equation from "../types/equation";
import React from "react";
import Upload from "../components/Upload";
import BlackWhiteImage from "../components/BlackWhiteImage";
import EncodeRepetition from "../components/repetition/EncodeRepetition";
import GenerateNoise from "../components/GenerateNoise";
import AddNoise from "../components/AddNoise";
import DecodeRepetition from "../components/repetition/DecodeRepetition";

function Repetition() {
  const [imageSrc, setImageSrc] = React.useState<string | null>(null);
  const [repetitionSrc, setRepetitionSrc] = React.useState<string | null>(null);
  const [noiseSrc, setNoiseSrc] = React.useState<string | null>(null);
  const [addedNoiseSrc, setAddedNoiseSrc] = React.useState<string | null>(null);
  const [decodedSrc, setDecodedSrc] = React.useState<string | null>(null);

  const setEncode = (
    canvas: HTMLCanvasElement | null
  ): HTMLCanvasElement | null => {
    try {
      let out = EncodeRepetition(canvas);
      setRepetitionSrc(out.toDataURL());
      return out;
    } catch (e) {
      setRepetitionSrc(null);
      return null;
    }
  };

  const setNoise = (
    canvas: HTMLCanvasElement | null,
    noiseAmount = 0.001
  ): HTMLCanvasElement | null => {
    try {
      let outNoise = GenerateNoise(canvas, noiseAmount);
      setNoiseSrc(outNoise.toDataURL());
      return outNoise;
    } catch (e) {
      setNoiseSrc(null);
      return null;
    }
  };

  const setAddNoise = (
    canvas: HTMLCanvasElement | null,
    canvas2: HTMLCanvasElement | null
  ) => {
    try {
      let outAddedNoise = AddNoise(canvas, canvas2);
      setAddedNoiseSrc(outAddedNoise.toDataURL());
      return outAddedNoise;
    } catch (e) {
      setAddedNoiseSrc(null);
      return null;
    }
  };

  const setDecode = (canvas: HTMLCanvasElement | null) => {
    try {
      let decodedImage = DecodeRepetition(canvas);
      setDecodedSrc(decodedImage.toDataURL());
      return decodedImage;
    } catch (e) {
      setDecodedSrc(null);
      return null;
    }
  };

  return (
    <MathJaxContext config={config}>
      <ThemeProvider theme={theme}>
        <Grid
          display="flex"
          justifyContent="center"
          alignItems="center"
          size="grow"
        >
          <Box component="section" sx={box}>
            <Box sx={heading}>Repetition Origins</Box>
            <Box sx={text}>
              Before Hamming published his work with Hamming codes, Repetition
              was a technique available if retransmission was too expensive.
              Under nomenclature, this can referred to as,
            </Box>
            <Box sx={equation}>
              <MathJax hideUntilTypeset="every">{"\\[(3,1)\\]"}</MathJax>
            </Box>
            <Box sx={text}>
              Repetition is almost never used, because there are always better
              options. Repetition still counts as FEC, so it will be included
              and documented.
            </Box>
            <br />
            <Box sx={heading}>Method</Box>
            <Box sx={text}>To encode, repeat the message bit 3 times,</Box>
            <Box sx={equation}>
              <MathJax hideUntilTypeset="every">
                {"\\[[1] \\rightarrow [1,1,1]\\]"}
              </MathJax>
            </Box>
            <Box sx={text}>
              Then when decoding each block, the bits that are in majority is
              the assumed message bit.
            </Box>
            <Box sx={equation}>
              <MathJax hideUntilTypeset="every">
                {"\\[[1,1,1] \\rightarrow [1]\\]"}
                {"\\[[1,1,0] \\rightarrow [1]\\]"}
                {"\\[[1,0,0] \\rightarrow [0]\\]"}
                {"\\[[0,0,0] \\rightarrow [0]\\]"}
              </MathJax>
            </Box>
            <Box sx={heading}>Test it out</Box>

            <Upload onUpload={(src: string) => setImageSrc(src)} />
            {imageSrc && (
              <BlackWhiteImage
                src={imageSrc}
                onCanvas={(canvas) => {
                  let encoded = setEncode(canvas);
                  let outNoise = setNoise(encoded);
                  let outAddedNoise = setAddNoise(encoded, outNoise);
                  setDecode(outAddedNoise);
                }}
              />
            )}
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
                <img
                  src={noiseSrc}
                  alt="inverted"
                  style={{ maxWidth: "100%" }}
                />
              </Box>
            )}
            {addedNoiseSrc && (
              <Box sx={{ marginTop: 2 }}>
                <img
                  src={addedNoiseSrc}
                  alt="inverted"
                  style={{ maxWidth: "100%" }}
                />
              </Box>
            )}
            {decodedSrc && (
              <Box sx={{ marginTop: 2 }}>
                <img
                  src={decodedSrc}
                  alt="inverted"
                  style={{ maxWidth: "100%" }}
                />
              </Box>
            )}
          </Box>
        </Grid>
      </ThemeProvider>
    </MathJaxContext>
  );
}

export default Repetition;
