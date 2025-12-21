import ConvertToBinary from "../conversions/ConvertToBinary";
import ConvertToImage from "../conversions/ConvertToImage";

// @param HTMLCanvasElement - The input image to add noise to
// @param noise - The amount of noise to add (0 to 1)
// @returns HTMLCanvasElement - Returns a new image the same size of just the noise.

function GenerateNoise(image: HTMLCanvasElement | null, noise: number) {
  if (image === null) {
    throw new Error("No image provided to AddNoise");
  }

  const binaryArray: number[][] = Array.from({ length: image.height }, () =>
    Array(image.width).fill(0)
  );

  // Generate Random Number of White Pixels
  for (let i = 0; i < noise * image.width * image.height; i++) {
    const x: number = Math.floor(Math.random() * image.width);
    const y: number = Math.floor(Math.random() * image.height);
    if (binaryArray[y][x] === 0) {
      binaryArray[y][x] = 1;
    } else {
      binaryArray[y][x] = 0;
    }
  }

  const out = ConvertToImage(binaryArray);
  return out;
}

export default GenerateNoise;
