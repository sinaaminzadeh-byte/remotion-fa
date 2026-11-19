import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  Sequence,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک ۱ — «کینتیک تایپوگرافی» (Bold / Kinetic type)
 * پس‌زمینه تیره، فونت خیلی درشت، کلمات با اسپرینگ می‌آیند و با ماسک می‌روند.
 * مناسب: ریلز، تیزر، اعلان کوتاه، لوگو-ریویل.
 */

const WORDS = ["ایده", "حرکت", "ویدیو"];
const ACCENT = "#FF4D2E";

const Word: React.FC<{ word: string; index: number }> = ({ word, index }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const enter = spring({ frame, fps, config: { damping: 11, mass: 0.6, stiffness: 120 } });
  const out = interpolate(frame, [38, 50], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.cubic),
  });

  const scale = interpolate(enter, [0, 1], [0.72, 1]);
  const blur = interpolate(enter, [0, 1], [18, 0]);
  const y = interpolate(out, [0, 1], [0, -120]);

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
      <div
        style={{
          fontFamily: FONT,
          fontWeight: 900,
          fontSize: 280,
          color: "#fff",
          letterSpacing: -6,
          transform: `translateY(${y}px) scale(${scale})`,
          filter: `blur(${blur}px)`,
          opacity: 1 - out,
          clipPath: `inset(${out * 55}% 0% ${out * 55}% 0%)`,
        }}
      >
        {word}
      </div>
      <div
        style={{
          fontFamily: FONT,
          fontWeight: 700,
          fontSize: 34,
          color: "rgba(255,255,255,0.45)",
          letterSpacing: 12,
          marginTop: 24,
          direction: "ltr",
        }}
      >
        {`0${index + 1} / 03`}
      </div>
    </AbsoluteFill>
  );
};

const ProgressBar: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <div style={{ position: "absolute", left: 0, right: 0, bottom: 0, height: 10, background: "rgba(255,255,255,0.12)" }}>
      <div style={{ width: `${(frame / 150) * 100}%`, height: "100%", background: ACCENT }} />
    </div>
  );
};

export const BoldKinetic: React.FC = () => {
  return (
    <AbsoluteFill style={{ background: "#0B0B0C", direction: "rtl" }}>
      {/* هاله‌ی نوری پشت کلمات */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at 50% 55%, ${ACCENT}22 0%, transparent 55%)`,
        }}
      />
      {WORDS.map((word, i) => (
        <Sequence key={word} from={i * 50} durationInFrames={50}>
          <Word word={word} index={i} />
        </Sequence>
      ))}
      <ProgressBar />
    </AbsoluteFill>
  );
};
