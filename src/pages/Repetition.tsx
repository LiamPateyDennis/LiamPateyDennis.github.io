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

function Repetition() {
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
          </Box>
        </Grid>
      </ThemeProvider>
    </MathJaxContext>
  );
}

export default Repetition;
