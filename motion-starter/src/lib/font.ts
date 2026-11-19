import { continueRender, delayRender, staticFile } from "remotion";

/**
 * فونت فارسی وزیرمتن را قبل از رندر لود می‌کنیم.
 * اگر فونت لود نشود، Remotion منتظر می‌ماند تا رندر خراب نشود.
 */
const handle = delayRender("Loading Vazirmatn");

const weights: { weight: string; file: string }[] = [
  { weight: "400", file: "fonts/Vazirmatn-Regular.ttf" },
  { weight: "700", file: "fonts/Vazirmatn-Bold.ttf" },
  { weight: "900", file: "fonts/Vazirmatn-Black.ttf" },
];

Promise.all(
  weights.map(({ weight, file }) => {
    const face = new FontFace(
      "Vazirmatn",
      `url(${staticFile(file)}) format("truetype")`,
      { weight },
    );
    return face.load().then((loaded) => document.fonts.add(loaded));
  }),
)
  .then(() => continueRender(handle))
  .catch((err) => {
    console.error("font load failed", err);
    continueRender(handle);
  });

export const FONT = "Vazirmatn, system-ui, sans-serif";
