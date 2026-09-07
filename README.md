# 16-bit Hack CPU (SystemVerilog)

A complete SystemVerilog implementation of the 16-bit Hack architecture, designed for high-performance hardware description and functional verification. This project follows the standard "Hack" architecture (from the Nand2Tetris project) while utilizing modern SystemVerilog features for modularity and clarity.

## 🚀 Project Overview
This repository contains a modular hardware design of a 16-bit CPU. It features a RISC-like instruction set, a dedicated ALU, and a split memory architecture (Instruction vs. Data). The design is fully synthesizable and optimized for deployment on FPGA hardware.

## 🏗 Architecture Highlights
- **16-bit ALU**: Supports 18 distinct operations including logic (AND, OR, XOR, NOT), arithmetic (Add, Sub, Bitwise Shift), and comparison.
- **Instruction Memory**: Separate memory spaces for instructions and data to prevent collision.
- **Register A & D**: Hardware registers for intermediate values and data storage.
- **Sequential Logic**: Clean separation between combinational logic and clocked registers for predictable timing.
- **SystemVerilog**: Leverages SystemVerilog for improved readability and structural organization.


## ⚙️ Simulation & Verification

More info soon

## 🚀 FPGA Implementation

Coming Soon

### 🛠 Hardware Target
- **Board:** Nexys A7-100T
- **FPGA:** AMD Artix-7 (XC7A100T)
- **Toolchain:** AMD Vivado Design Suite

## Disclaimer
This project is still a work in progress, I intend to keep updating it until it reaches a finalized state (FPGA Implementation). It also serves to test practices and software for an upcoming RISC-V CPU project.
