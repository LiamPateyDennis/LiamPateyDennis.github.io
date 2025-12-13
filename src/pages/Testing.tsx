import React from "react";
import { MathJaxContext, MathJax } from "better-react-mathjax";

const config = {
  loader: { load: ["input/asciimath", "output/chtml"] },
};

function Testing() {
  return (
    <MathJaxContext config={config}>
      <div>
        <p>
          Inline math:{" "}
          <MathJax hideUntilTypeset="first" inline>
            {"\\(a^2 + b^2 = c^2\\)"}
          </MathJax>
        </p>
        <p>
          Block math:
          <MathJax hideUntilTypeset="every">
            {"\\[\\int_0^\\infty e^{-x^2} dx = \\frac{\\sqrt{\\pi}}{2}\\]"}
          </MathJax>
        </p>
      </div>
    </MathJaxContext>
  );
}

export default Testing;
