import ConvertToBinary from "../../conversions/ConvertToBinary";
import ConvertToImage from "../../conversions/ConvertToImage";

function DecodeRepetition(image: HTMLCanvasElement | null): HTMLCanvasElement {
  let srcCanvas: HTMLCanvasElement;

  if (image instanceof HTMLCanvasElement) {
    srcCanvas = image;
  } else {
    throw new Error("No image provided to DecodeRepetition");
  }

  const binaryArray = ConvertToBinary(srcCanvas);
  const unitWidth = srcCanvas.width / 3;

  const RepCorrect = (
    setBinary: number,
    UnitWidth: number,
    x: number,
    y: number
  ) => {
    binaryArray[y][x] = setBinary;
    binaryArray[y][x + UnitWidth] = setBinary;
    binaryArray[y][x + 2 * UnitWidth] = setBinary;
  };

  for (let y = 0; y < srcCanvas.height; y++) {
    for (let x = 0; x < unitWidth; x++) {
      if (
        (binaryArray[y][x] +
          binaryArray[y][x + unitWidth] +
          binaryArray[y][x + 2 * unitWidth]) %
          3 !==
        0
      ) {
        (binaryArray[y][x] +
          binaryArray[y][x + unitWidth] +
          binaryArray[y][x + 2 * unitWidth]) %
          3 ===
        1
          ? RepCorrect(0, unitWidth, x, y)
          : RepCorrect(1, unitWidth, x, y);
      }
    }
  }

  const out = ConvertToImage(binaryArray);
  return out;
}

export default DecodeRepetition;
