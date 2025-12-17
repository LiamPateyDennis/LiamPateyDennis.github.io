const ProcessImage = (img: HTMLImageElement) => {
  const canvas = document.createElement("canvas");
  const ctx = canvas.getContext("2d");
  if (!ctx) return;
  
  canvas.width = img.width;
  canvas.height = img.height;
  ctx.drawImage(img, 0, 0);

  // Example: invert colors
  const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
  const data = imageData.data;
  for (let i = 0; i < data.length; i += 4) {
    data[i] = 255 - data[i];     // Red
    data[i+1] = 255 - data[i+1]; // Green
    data[i+2] = 255 - data[i+2]; // Blue
  }
  ctx.putImageData(imageData, 0, 0);
};

export default ProcessImage