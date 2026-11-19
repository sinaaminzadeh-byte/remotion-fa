import React from "react";
import { AbsoluteFill, Easing, interpolate, useCurrentFrame } from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۰۷ — ممفیس / دهه‌ی ۹۰
 * الگوی شطرنجی، شکل‌های تصادفی، رنگ‌های سیتی، بافت هاف‌تون.
 * زبان بصری: بازیگوش، نوستالژیک، سرگرمی، فشن.
 */

const BG = "#FFD9E8";
const NAVY = "#1B1B4B";
const TEAL = "#00C2A8";
const ORANGE = "#FF7A2F";

const ZigZag: React.FC<{ x: number; y: number; w: number; color: string; rotate: number }> = ({ x, y, w, color, rotate }) => (
  <svg width={w} height={w * 0.4} style={{ position: "absolute", left: x, top: y, transform: `rotate(${rotate}deg)` }}>
    <polyline points={`0,${w * 0.35} ${w * 0.125},0 ${w * 0.25},${w * 0.35} ${w * 0.375},0 ${w * 0.5},${w * 0.35} ${w * 0.625},0 ${w * 0.75},${w * 0.35} ${w * 0.875},0 ${w},${w * 0.35}`} fill="none" stroke={color} strokeWidth={7} strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

export const Memphis90s: React.FC = () => {
  const frame = useCurrentFrame();
  const t = frame / 30;

  return (
    <AbsoluteFill style={{ background: BG, direction: "rtl", fontFamily: FONT, overflow: "hidden" }}>
      {/* پترن هاچ */}
      <AbsoluteFill
        style={{
          backgroundImage: `repeating-linear-gradient(45deg, ${NAVY}12 0px, ${NAVY}12 2px, transparent 2px, transparent 14px)`,
        }}
      />

      {/* شکل‌های ممفیس */}
      <div style={{ position: "absolute", left: 90, top: 90, width: 130, height: 130, borderRadius: "50%", background: TEAL, opacity: 0.85, transform: `translateY(${Math.sin(t * 1.4) * 12}px)` }} />
      <div style={{ position: "absolute", right: 120, top: 150, width: 0, height: 0, borderLeft: "85px solid transparent", borderRight: "85px solid transparent", borderBottom: `150px solid ${ORANGE}`, transform: `rotate(${t * 14}deg)` }} />
      <div style={{ position: "absolute", right: 240, bottom: 90, width: 150, height: 150, background: NAVY, transform: `rotate(${t * -8}deg)` }} />
      <ZigZag x={110} y={200} w={300} color={NAVY} rotate={-6} />
      <ZigZag x={1300} y={800} w={240} color={TEAL} rotate={8} />
      {/* نقاط */}
      {Array.from({ length: 5 }).map((_, r) =>
        Array.from({ length: 4 }).map((_, c) => (
          <div key={`${r}-${c}`} style={{ position: "absolute", left: 1560 + c * 34, top: 300 + r * 34, width: 14, height: 14, borderRadius: "50%", background: NAVY }} />
        )),
      )}

      <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
        <div style={{ textAlign: "center" }}>
          <div
            style={{
              display: "inline-block",
              background: "#fff",
              border: `7px solid ${NAVY}`,
              padding: "16px 44px",
              fontSize: 36,
              fontWeight: 900,
              color: NAVY,
              letterSpacing: 6,
              marginBottom: 34,
              transform: `rotate(-3deg) scale(${interpolate(frame, [0, 14], [0.7, 1], { extrapolateRight: "clamp", easing: Easing.out(Easing.back(2)) })})`,
              direction: "ltr",
            }}
          >
            MEMPHIS 90s
          </div>
          <div
            style={{
              fontSize: 158,
              fontWeight: 900,
              color: NAVY,
              lineHeight: 1.1,
              letterSpacing: -2,
              WebkitTextStroke: `3px ${NAVY}`,
              transform: `rotate(${interpolate(frame, [0, 150], [-2, 2])}deg)`,
            }}
          >
            ایده، حرکت،{" "}
            <span style={{ color: ORANGE }}>ویدیو</span>
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
