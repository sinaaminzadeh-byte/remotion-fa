import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک ۳ — «مینیمال ادیتوریال» (Minimal / Editorial)
 * کاغذ روشن، خطوط نازک، فضای خالی زیاد، ورود خط‌به‌خط با ماسک.
 * مناسب: برند شخصی، مستند، محتوای آموزشی، ارائه‌ی شرکتی.
 */

const LINES = ["اولین موشن‌گرافیکت", "با کد ساخته می‌شود."];

const Line: React.FC<{ text: string; delay: number }> = ({ text, delay }) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [delay, delay + 16], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  return (
    <div style={{ overflow: "hidden" }}>
      <div
        style={{
          transform: `translateY(${(1 - p) * 100}%)`,
          fontSize: 116,
          fontWeight: 700,
          lineHeight: 1.22,
          letterSpacing: -1.5,
          color: "#141414",
        }}
      >
        {text}
      </div>
    </div>
  );
};

export const MinimalEditorial: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const rule = interpolate(frame, [8, 34], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  const meta = interpolate(frame, [30, 46], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const footer = interpolate(frame, [60, 80], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const dot = 6 + Math.sin((frame / fps) * Math.PI * 2) * 2;

  return (
    <AbsoluteFill style={{ background: "#F4F1EA", direction: "rtl", fontFamily: FONT }}>
      <AbsoluteFill style={{ padding: "96px 120px" }}>
        {/* سربرگ */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", direction: "ltr" }}>
          <div style={{ fontSize: 22, letterSpacing: 6, color: "#8A8578", fontWeight: 700 }}>MOTION STUDY</div>
          <div style={{ display: "flex", alignItems: "center", gap: 12, fontSize: 22, color: "#8A8578" }}>
            <div style={{ width: dot * 2, height: dot * 2, borderRadius: "50%", background: "#C8452B" }} />
            <span style={{ direction: "rtl" }}>نمونه</span>
          </div>
        </div>

        <div style={{ height: 2, background: "#141414", marginTop: 28, transform: `scaleX(${rule})`, transformOrigin: "right" }} />

        <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "center" }}>
          {LINES.map((line, i) => (
            <Line key={line} text={line} delay={14 + i * 10} />
          ))}

          <div style={{ display: "flex", gap: 28, marginTop: 54, opacity: meta, direction: "rtl" }}>
            {["ایده", "حرکت", "ویدیو"].map((step, i) => (
              <div key={step} style={{ display: "flex", alignItems: "baseline", gap: 12, color: "#5B574D", fontSize: 30 }}>
                <span style={{ fontWeight: 900, color: "#C8452B" }}>{`0${i + 1}`}</span>
                <span>{step}</span>
              </div>
            ))}
          </div>
        </div>

        <div style={{ height: 1, background: "#CFC9BC", marginBottom: 22 }} />
        <div style={{ display: "flex", justifyContent: "space-between", fontSize: 24, color: "#8A8578", opacity: footer, direction: "ltr" }}>
          <span>Remotion · React</span>
          <span>1920 × 1080 · 30fps</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
