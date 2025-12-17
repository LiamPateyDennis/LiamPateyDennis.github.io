/**
 * Accepts an input image (HTMLCanvasElement, ImageData, or HTMLImageElement),
 * tiles it, enforces black/white pixels, and returns a new HTMLCanvasElement.
 */
function FuncRepetition(
  image: HTMLCanvasElement | ImageData | HTMLImageElement
): HTMLCanvasElement {
  let srcCanvas: HTMLCanvasElement;

  if (image instanceof HTMLCanvasElement) {
    srcCanvas = image;
  } else {
    srcCanvas = document.createElement("canvas");
    const ctx = srcCanvas.getContext("2d")!;

    if ((image as ImageData).data && (image as ImageData).width) {
      const imgData = image as ImageData;
      srcCanvas.width = imgData.width;
      srcCanvas.height = imgData.height;
      ctx.putImageData(imgData, 0, 0);
    } else {
      const imgEl = image as HTMLImageElement;
      srcCanvas.width = imgEl.naturalWidth || imgEl.width;
      srcCanvas.height = imgEl.naturalHeight || imgEl.height;
      ctx.drawImage(imgEl, 0, 0);
    }
  }

  const tileX = 3;
  const tileY = 3;
  const out = document.createElement("canvas");
  out.width = srcCanvas.width * tileX;
  out.height = srcCanvas.height * tileY;
  const outCtx = out.getContext("2d")!;

  for (let y = 0; y < tileY; y++) {
    for (let x = 0; x < tileX; x++) {
      outCtx.drawImage(srcCanvas, x * srcCanvas.width, y * srcCanvas.height);
    }
  }
  // Ensure final output is strictly black or white (no greys)
  const imageData = outCtx.getImageData(0, 0, out.width, out.height);
  console.log(imageData);
  const data = imageData.data;
  for (let i = 0; i < data.length; i += 1) {}
  outCtx.putImageData(imageData, 0, 0);

  return out;
}

export default FuncRepetition;
