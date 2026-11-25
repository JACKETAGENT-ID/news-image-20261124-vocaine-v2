// Entry program for the make.fun news-image-20261124 competition.
// Copies the pre-drawn entry.png (1024x1024, under 1 MiB) to the
// grader's output directory. Node 22, standard library only, no network.
import { copyFileSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(HERE, "entry.png");
const OUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const OUT = join(OUT_DIR, "entry.png");

const buf = readFileSync(SRC);
if (buf.length < 8 || buf[0] !== 0x89 || buf[1] !== 0x50 || buf[2] !== 0x4e
    || buf[3] !== 0x47 || buf[4] !== 0x0d || buf[5] !== 0x0a
    || buf[6] !== 0x1a || buf[7] !== 0x0a) {
  throw new Error("entry.png is not a PNG file");
}

// Width and height live in the IHDR chunk: bytes 16-19 and 20-23.
const width = buf.readUInt32BE(16);
const height = buf.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error(`entry.png is ${width}x${height}, over the 1024x1024 limit`);
}
if (buf.length > 1048576) {
  throw new Error(`entry.png is ${buf.length} bytes, over the 1 MiB limit`);
}

mkdirSync(OUT_DIR, { recursive: true });
copyFileSync(SRC, OUT);
const outStat = statSync(OUT);
console.log(`entry.png: ${width}x${height}, ${buf.length} bytes -> ${OUT} (${outStat.size} bytes)`);
