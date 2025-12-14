import Box from "@mui/material/Box";
import theme from "../types/theme";
import { ThemeProvider } from "@mui/material";
import Grid from "@mui/material/Grid";
import text from "../types/text";
import box from "../types/box";
import heading from "../types/heading";
import { MathJaxContext, MathJax } from "better-react-mathjax";
import config from "../types/configMath";
import equation from "../types/equation"

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
            <Box sx={heading}>Repetition</Box>
            <Box sx={text}>
              Before Hamming published his work with Hamming codes, Repetition
              was a technique available if retransmission was too expensive.
              Under nomenclature, this can referred to as,
            <Box sx={equation}>
            <MathJax hideUntilTypeset="every">
                {"\\[\(3,1\)\\]"}
            </MathJax>
            </Box>
            </Box>
          </Box>
        </Grid>
      </ThemeProvider>
    </MathJaxContext>
  );
}

export default Repetition;
