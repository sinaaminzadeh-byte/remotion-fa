import React from "react";
import { Composition } from "remotion";
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
import { StyleReel, SLOT, ITEM_COUNT } from "./StyleReel";

const FPS = 30;
const DURATION = 150; // ۵ ثانیه

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* ───── سبک‌های پایه ───── */}
      <Composition id="BoldKinetic" component={BoldKinetic} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="BoldKinetic-Vertical" component={BoldKinetic} durationInFrames={DURATION} fps={FPS} width={1080} height={1920} />
      <Composition id="GradientGlass" component={GradientGlass} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="MinimalEditorial" component={MinimalEditorial} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />

      {/* ───── کاتالوگ سبک‌های گرافیکی ───── */}
      <Composition id="FlatCorporate" component={FlatCorporate} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="NeonFuturistic" component={NeonFuturistic} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="PaperCollage" component={PaperCollage} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="KraftStudio" component={KraftStudio} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="NeoBrutalist" component={NeoBrutalist} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="Voxel3D" component={Voxel3D} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="Memphis90s" component={Memphis90s} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="InfographicData" component={InfographicData} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="SwissGrid" component={SwissGrid} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
      <Composition id="ClaySoft" component={ClaySoft} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />

      {/* ریل معرفی همه‌ی سبک‌ها — ۱۳ × ۱.۵ ثانیه */}
      <Composition id="StyleReel" component={StyleReel} durationInFrames={SLOT * ITEM_COUNT} fps={FPS} width={1920} height={1080} />
    </>
  );
};
