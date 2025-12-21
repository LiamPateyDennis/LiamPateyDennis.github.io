// @param HTMLCanvasElement - The input image to convert
// @returns 2d binary array

function ConvertToBinary(image: HTMLCanvasElement) {
    const width = image.width;
    const height = image.height;
    const ctx = image.getContext("2d")!;
    const imageData = ctx.getImageData(0, 0, width, height);
    const data = imageData.data;

    const binaryArray: number[][] = new Array(height);
    for (let y = 0; y < height; y++) {
        binaryArray[y] = new Array(width);
        for (let x = 0; x < width; x++) {
            const idx = (y * width + x) * 4;
            const sum = data[idx] + data[idx + 1] + data[idx + 2];
            binaryArray[y][x] = sum > 382 ? 1 : 0;
        }
    }

    return binaryArray;
}

export default ConvertToBinary;
