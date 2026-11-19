import React from "react";
import { AbsoluteFill, Easing, interpolate, useCurrentFrame } from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۰۹ — سوئیسی / گرید (Swiss / International Typographic)
 * گرید دقیق، قرمز و مشکی روی سفید، تایپ چپ‌چین و منظم، فضای خالی.
 * زبان بصری: معماری، طراحی صنعتی، موزه، برند لوکس مینیمال.
 */

const RED = "#E4332B";
const INK = "#111111";

export const SwissGrid: React.FC = () => {
  const frame = useCurrentFrame();
  const rule = interpolate(frame, [0, 26], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  const circle = interpolate(frame, [10, 46], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  const textY = interpolate(frame, [16, 46], [70, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  const textO = interpolate(frame, [16, 42], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ background: "#FBFBF9", direction: "rtl", fontFamily: FONT, overflow: "hidden" }}>
      {/* نشانه‌های گرید */}
      {[1, 2, 3, 4, 5].map((i) => (
        <div key={i} style={{ position: "absolute", left: `${i * 16.66}%`, top: 0, bottom: 0, width: 1, background: "#11111112" }} />
      ))}

      <AbsoluteFill style={{ padding: "84px 96px" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", direction: "ltr" }}>
          <span style={{ fontSize: 22, letterSpacing: 5, fontWeight: 700, color: INK }}>MOTION / 01</span>
          <span style={{ fontSize: 22, letterSpacing: 5, color: "#8A8A8A" }}>SWISS SYSTEM</span>
        </div>

        <div style={{ height: 8, background: RED, marginTop: 26, transform: `scaleX(${rule})`, transformOrigin: "left" }} />

        <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 70 }}>
          {/* دایره‌ی قرمز */}
          <div style={{ width: 340, height: 340, borderRadius: "50%", background: RED, transform: `scale(${circle})`, flexShrink: 0 }} />

          <div style={{ transform: `translateY(${textY}px)`, opacity: textO }}>
            <div style={{ fontSize: 122, fontWeight: 700, color: INK, lineHeight: 1.16, letterSpacing: -3 }}>
              ایده
              <br />
              حرکت
              <br />
              ویدیو
            </div>
            <div style={{ fontSize: 26, color: "#7A7A7A", marginTop: 34, maxWidth: 620, lineHeight: 1.8 }}>
              نظم، گرید، و فضای خالی — سه ابزار اصلی.
            </div>
          </div>
        </div>

        <div style={{ display: "flex", justifyContent: "space-between", borderTop: `2px solid ${INK}`, paddingTop: 18, fontSize: 22, color: "#8A8A8A", direction: "ltr" }}>
          <span>HELVETICA / GRID</span>
          <span>1920 × 1080</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
