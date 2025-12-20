// @param HTMLCanvasElement - The input image to convert
// @returns 2d binary array

function ConvertToBinary(image: HTMLCanvasElement){

  const out = document.createElement("canvas");
  out.width = image.width;
  out.height = image.height;
  const outCtx = out.getContext("2d")!;

  const imageData = outCtx.getImageData(0, 0, out.width, out.height);
  const data = imageData.data;

  let binaryArray: number[][] = [];

  for (let i = 0; i < data.length; i += 4) {
        if (data[i] + data[i + 1] + data[i + 2] > 382) {
            binaryArray[(i/4) % out.width][(i/4) % out.height] = 1; // White pixel
        } else {
            binaryArray[(i/4) % out.width][(i/4) % out.height] = 0; // Black pixel
        }
    }
    return binaryArray;

}
  

export default ConvertToBinary;
