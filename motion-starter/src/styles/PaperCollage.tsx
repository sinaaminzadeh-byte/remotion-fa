import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۰۳ — بافت کاغذ / کلاژ ادیتوریال (Editorial Collage)
 * بافت کاغذ، حاشیه‌ی ناهموار، خط‌های دستی، رنگ‌های خاکی.
 * زبان بصری: انسانی، فرهنگی، مجله‌ای، برند شخصی.
 */

const PAPER = "#EDE6D8";
const INK = "#1F1B16";
const RED = "#B5342B";

const Tape: React.FC<{ style: React.CSSProperties }> = ({ style }) => (
  <div
    style={{
      position: "absolute",
      width: 200,
      height: 46,
      background: "rgba(214,198,160,0.75)",
      boxShadow: "0 2px 8px rgba(0,0,0,0.12)",
      ...style,
    }}
  />
);

export const PaperCollage: React.FC = () => {
  const frame = useCurrentFrame();
  const rotate = interpolate(frame, [0, 150], [-2.4, -1.2]);
  const ink = interpolate(frame, [10, 50], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ background: PAPER, direction: "rtl", fontFamily: FONT, overflow: "hidden" }}>
      {/* بافت دانه‌ای کاغذ */}
      <AbsoluteFill
        style={{
          backgroundImage:
            "radial-gradient(rgba(120,100,70,0.16) 1px, transparent 1px), radial-gradient(rgba(120,100,70,0.10) 1px, transparent 1px)",
          backgroundSize: "7px 7px, 13px 13px",
          backgroundPosition: "0 0, 4px 3px",
        }}
      />
      {/* لکه‌ی لبه */}
      <AbsoluteFill style={{ background: `radial-gradient(ellipse at 50% 50%, transparent 55%, rgba(120,98,60,0.22) 100%)` }} />

      <Tape style={{ top: 60, right: 180, transform: "rotate(-6deg)" }} />
      <Tape style={{ bottom: 90, left: 150, transform: "rotate(4deg)" }} />

      <AbsoluteFill style={{ padding: "100px 120px" }}>
        <div style={{ display: "flex", justifyContent: "space-between", fontSize: 24, letterSpacing: 5, color: "#7C6F5C", direction: "ltr", fontWeight: 700 }}>
          <span>ISSUE 04</span>
          <span>MOTION STUDY</span>
        </div>

        <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }}>
          {/* کارت متن چرخیده */}
          <div
            style={{
              background: "#FBF7EE",
              padding: "70px 90px",
              transform: `rotate(${rotate}deg)`,
              boxShadow: "0 26px 60px rgba(60,45,25,0.22)",
              border: `1px solid rgba(120,98,60,0.25)`,
              position: "relative",
            }}
          >
            <div style={{ fontSize: 132, fontWeight: 900, color: INK, lineHeight: 1.2, letterSpacing: -2 }}>
              ایده، حرکت،{" "}
              <span style={{ position: "relative", display: "inline-block" }}>
                ویدیو
                <div
                  style={{
                    position: "absolute",
                    bottom: 6,
                    right: -4,
                    left: -4,
                    height: 22,
                    background: RED,
                    opacity: 0.28,
                    transform: `scaleX(${ink})`,
                    transformOrigin: "right",
                  }}
                />
              </span>
            </div>
            <div style={{ fontSize: 30, color: "#6B5F4E", marginTop: 26, lineHeight: 1.7, maxWidth: 780 }}>
              هر فریم یک صفحه از مجله‌ی توست.
            </div>

            {/* دایره‌ی دستی */}
            <svg width="150" height="150" style={{ position: "absolute", top: -46, left: -52 }}>
              <circle cx="75" cy="75" r="66" fill="none" stroke={RED} strokeWidth="2.5" strokeDasharray="300" strokeDashoffset={interpolate(frame, [20, 70], [300, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })} transform="rotate(-40 75 75)" opacity="0.8" />
            </svg>
          </div>
        </div>

        <div style={{ display: "flex", justifyContent: "space-between", fontSize: 24, color: "#7C6F5C", direction: "rtl" }}>
          <span>کاغذ · کلاژ · دست‌ساز</span>
          <span style={{ direction: "ltr" }}>2026 · PAGE 01</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
