import React from "react";
import { AbsoluteFill, Sequence, interpolate, useCurrentFrame } from "remotion";
import { FONT } from "./lib/font";
import { BoldKinetic } from "./styles/BoldKinetic";
import { GradientGlass } from "./styles/GradientGlass";
import { MinimalEditorial } from "./styles/MinimalEditorial";
import { FlatCorporate } from "./styles/FlatCorporate";
import { NeonFuturistic } from "./styles/NeonFuturistic";
import { PaperCollage } from "./styles/PaperCollage";
import { KraftStudio } from "./styles/KraftStudio";
import { NeoBrutalist } from "./styles/NeoBrutalist";
import { Voxel3D } from "./styles/Voxel3D";
import { Memphis90s } from "./styles/Memphis90s";
import { InfographicData } from "./styles/InfographicData";
import { SwissGrid } from "./styles/SwissGrid";
import { ClaySoft } from "./styles/ClaySoft";

/**
 * ریل اسکای — همه‌ی سبک‌ها پشت سر هم، هر کدام ۴۵ فریم (۱.۵ ثانیه)
 */

const ITEMS: { Comp: React.FC; fa: string; en: string; dark: boolean }[] = [
  { Comp: BoldKinetic, fa: "کینتیک تایپوگرافی", en: "BOLD KINETIC", dark: true },
  { Comp: NeoBrutalist, fa: "نئو-بروتالیست", en: "NEO-BRUTALISM", dark: false },
  { Comp: NeonFuturistic, fa: "نئون / سایبرپانک", en: "NEON CYBER", dark: true },
  { Comp: GradientGlass, fa: "گرادیان + شیشه", en: "GLASSMORPHISM", dark: true },
  { Comp: Voxel3D, fa: "وکسل / ایزومتریک", en: "VOXEL 3D", dark: false },
  { Comp: Memphis90s, fa: "ممفیس / دهه ۹۰", en: "MEMPHIS 90s", dark: false },
  { Comp: PaperCollage, fa: "کاغذ / کلاژ ادیتوریال", en: "EDITORIAL PAPER", dark: false },
  { Comp: KraftStudio, fa: "کرافت / کارگاه", en: "KRAFT ARTISAN", dark: false },
  { Comp: SwissGrid, fa: "سوئیسی / گرید", en: "SWISS GRID", dark: false },
  { Comp: InfographicData, fa: "اینفوگرافیک / داده", en: "DATA INFOGRAPHIC", dark: true },
  { Comp: FlatCorporate, fa: "تخت مدرن", en: "CORPORATE FLAT", dark: false },
  { Comp: ClaySoft, fa: "کلی / نرم سه‌بعدی", en: "CLAYMORPHISM", dark: false },
  { Comp: MinimalEditorial, fa: "مینیمال ادیتوریال", en: "MINIMAL", dark: false },
];

export const SLOT = 45;
export const ITEM_COUNT = ITEMS.length;

const Label: React.FC<{ fa: string; en: string; dark: boolean; index: number }> = ({ fa, en, dark, index }) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" });
  return (
    <div
      style={{
        position: "absolute",
        left: 46,
        bottom: 40,
        display: "flex",
        alignItems: "center",
        gap: 16,
        padding: "14px 26px",
        borderRadius: 999,
        background: dark ? "rgba(255,255,255,0.14)" : "rgba(0,0,0,0.72)",
        border: `1px solid ${dark ? "rgba(255,255,255,0.35)" : "rgba(255,255,255,0.18)"}`,
        backdropFilter: "blur(10px)",
        opacity: p,
        transform: `translateY(${interpolate(p, [0, 1], [14, 0])}px)`,
        fontFamily: FONT,
        zIndex: 100,
      }}
    >
      <span style={{ fontSize: 22, fontWeight: 900, color: "#fff", direction: "ltr", letterSpacing: 2 }}>
        {String(index + 1).padStart(2, "0")}
      </span>
      <span style={{ width: 1, height: 22, background: "rgba(255,255,255,0.4)" }} />
      <span style={{ fontSize: 26, fontWeight: 700, color: "#fff" }}>{fa}</span>
      <span style={{ fontSize: 18, color: "rgba(255,255,255,0.65)", direction: "ltr", letterSpacing: 2 }}>{en}</span>
    </div>
  );
};

const Slot: React.FC<{ item: (typeof ITEMS)[number]; index: number }> = ({ item, index }) => {
  const frame = useCurrentFrame();
  const fadeIn = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });
  const fadeOut = interpolate(frame, [SLOT - 6, SLOT], [1, 0], { extrapolateLeft: "clamp" });
  return (
    <AbsoluteFill style={{ opacity: Math.min(fadeIn, fadeOut) }}>
      <item.Comp />
      <Label fa={item.fa} en={item.en} dark={item.dark} index={index} />
    </AbsoluteFill>
  );
};

export const StyleReel: React.FC = () => {
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      {ITEMS.map((item, i) => (
        <Sequence key={i} from={i * SLOT} durationInFrames={SLOT}>
          <Slot item={item} index={i} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
