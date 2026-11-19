import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۰۱ — تخت مدرن / Corporate Flat
 * شکل‌های هندسی ساده، رنگ تخت، بدون گرادیان، بدون سایه‌ی نرم.
 * زبان بصری: قابل‌اعتماد، روشن، «اینفوگرافیک».
 */

const COLORS = { bg: "#F1F4F9", ink: "#10203A", blue: "#2B5CE6", mint: "#25C7A0" };

export const FlatCorporate: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const s1 = spring({ frame, fps, config: { damping: 13, mass: 0.5 } });
  const s2 = spring({ frame: frame - 12, fps, config: { damping: 13, mass: 0.5 } });
  const s3 = spring({ frame: frame - 24, fps, config: { damping: 13, mass: 0.5 } });
  const bar = interpolate(frame, [40, 90], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  return (
    <AbsoluteFill style={{ background: COLORS.bg, direction: "rtl", fontFamily: FONT, overflow: "hidden" }}>
      {/* دایره‌ی بزرگ */}
      <div
        style={{
          position: "absolute",
          left: -140,
          top: -120,
          width: 620,
          height: 620,
          borderRadius: "50%",
          background: COLORS.blue,
          opacity: 0.1,
        }}
      />
      {/* مثلث */}
      <div
        style={{
          position: "absolute",
          right: 120,
          bottom: -60,
          width: 0,
          height: 0,
          borderLeft: "150px solid transparent",
          borderRight: "150px solid transparent",
          borderBottom: `260px solid ${COLORS.mint}`,
          opacity: 0.16,
          transform: `rotate(${interpolate(frame, [0, 150], [-6, 6])}deg)`,
        }}
      />

      <AbsoluteFill style={{ padding: "110px 130px" }}>
        {/* آیکون/برچسب */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 18,
            transform: `translateX(${interpolate(s1, [0, 1], [40, 0])}px)`,
            opacity: s1,
          }}
        >
          <div style={{ width: 46, height: 46, borderRadius: 12, background: COLORS.blue }} />
          <div style={{ fontSize: 28, fontWeight: 700, letterSpacing: 4, color: COLORS.blue }}>MOTION</div>
        </div>

        <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "center" }}>
          <div
            style={{
              fontSize: 128,
              fontWeight: 900,
              lineHeight: 1.18,
              color: COLORS.ink,
              letterSpacing: -2,
              opacity: s2,
              transform: `translateY(${interpolate(s2, [0, 1], [56, 0])}px)`,
            }}
          >
            ایده، حرکت، ویدیو
          </div>

          {/* نوار پیشرفت با شکل‌های تخت */}
          <div style={{ display: "flex", gap: 20, marginTop: 64, opacity: s3 }}>
            {[0, 1, 2].map((i) => (
              <div
                key={i}
                style={{
                  height: 20,
                  width: 210,
                  background: [COLORS.blue, COLORS.mint, "#B9C4D6"][i],
                  borderRadius: 4,
                  transform: `scaleX(${interpolate(bar, [0, 1], [0, 1])})`,
                  transformOrigin: "right",
                }}
              />
            ))}
          </div>
        </div>

        <div style={{ fontSize: 26, color: "#7A879C", opacity: s3, fontWeight: 400 }}>
          Flat · Geometric · Confident
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
