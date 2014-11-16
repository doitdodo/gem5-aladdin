#!/usr/bin/env python
# SHOC design sweep definition. Import this file at the top of
# generate_design_sweep.

from design_sweep_types import *

# Sweep parameters. If a certain parameter should not be swept, set the value of
# step to NO_SWEEP, and the value of start will be used as a constant. end will
# be ignored. step should never be less than 1.
cache_size = SweepParam(
     "cache_size", start=16384, end=16384, step=NO_SWEEP, step_type=EXP_SWEEP)
cache_assoc = SweepParam(
    "cache_assoc", start=8, end=8, step=2, step_type=EXP_SWEEP)
cache_line_sz = SweepParam(
    "line_size_bytes", start=8, end=8, step=1, step_type=LINEAR_SWEEP)
pipelining = SweepParam(
    "pipelining", start=1, end=1, step=1, step_type=LINEAR_SWEEP)
unrolling = SweepParam(
    "unrolling", start=1, end=64, step=2, step_type=EXP_SWEEP)
partition = SweepParam(
    "partition", start=1, end=64, step=2, step_type=EXP_SWEEP)
cache_hit_latency = SweepParam(
    "cache_hit_latency", start=1, end=1, step=1, step_type=LINEAR_SWEEP)
tlb_entries = SweepParam(
    "tlb_entries", start=32, end=32, step=2, step_type=EXP_SWEEP)
tlb_max_outstanding_walks = SweepParam(
    "tlb_max_outstanding_walks", start=2, end=2, step=1, step_type=LINEAR_SWEEP)
load_bandwidth = SweepParam(
    "load_bandwidth", start=1, end=8, step=2, step_type=EXP_SWEEP)
store_bandwidth = SweepParam(
    "store_bandwidth", start=1, end=8, step=2, step_type=EXP_SWEEP)
store_queue_size = SweepParam(
    "store_queue_size", start=8, end=32, step=2, step_type=EXP_SWEEP)
load_queue_size = SweepParam(
    "load_queue_size", start=8, end=32, step=2, step_type=EXP_SWEEP)
dma_setup_latency = SweepParam(
    "dma_setup_latency", start=1, end=1, step=1, step_type=LINEAR_SWEEP)

# Benchmarks

bb_gemm = Benchmark("bb_gemm", "bb_gemm")
bb_gemm.set_kernels(["bb_gemm"])
bb_gemm.add_array("x", 1024, 4, PARTITION_CYCLIC)
bb_gemm.add_array("y", 1024, 4, PARTITION_CYCLIC)
bb_gemm.add_array("z", 1024, 4, PARTITION_CYCLIC)
bb_gemm.add_loop("bb_gemm", 11)
bb_gemm.add_loop("bb_gemm", 12, UNROLL_FLATTEN)
bb_gemm.add_loop("bb_gemm", 14, UNROLL_FLATTEN)

fft = Benchmark("fft", "fft")
fft.set_kernels([
    "fft1D_512", "step1", "step2", "step3", "step4", "step5", "step6",
    "step7", "step8", "step9", "step10", "step11"])
fft.add_array("work_x", 512, 4, PARTITION_CYCLIC)
fft.add_array("work_y", 512, 4, PARTITION_CYCLIC)
fft.add_array("DATA_x", 512, 4, PARTITION_CYCLIC)
fft.add_array("DATA_y", 512, 4, PARTITION_CYCLIC)
fft.add_array("data_x", 8, 4, PARTITION_COMPLETE)
fft.add_array("data_y", 8, 4, PARTITION_COMPLETE)
fft.add_array("smem", 576, 4, PARTITION_CYCLIC)
fft.add_array("reversed", 8, 4, PARTITION_COMPLETE)
fft.add_array("sin_64", 448, 4, PARTITION_COMPLETE)
fft.add_array("cos_64", 448, 4, PARTITION_COMPLETE)
fft.add_array("sin_512", 448, 4, PARTITION_COMPLETE)
fft.add_array("cos_512", 448, 4, PARTITION_COMPLETE)
fft.add_loop("step1", 16)
fft.add_loop("step1", 18, UNROLL_FLATTEN)
fft.add_loop("step1", 26, UNROLL_FLATTEN)
fft.add_loop("step1", 36, UNROLL_FLATTEN)
fft.add_loop("step2", 53)
fft.add_loop("step2", 54, UNROLL_FLATTEN)
fft.add_loop("step3", 75)
fft.add_loop("step3", 76, UNROLL_FLATTEN)
fft.add_loop("step3", 83, UNROLL_FLATTEN)
fft.add_loop("step4", 100)
fft.add_loop("step4", 101, UNROLL_FLATTEN)
fft.add_loop("step5", 122)
fft.add_loop("step5", 123, UNROLL_FLATTEN)
fft.add_loop("step5", 130, UNROLL_FLATTEN)
fft.add_loop("step6", 149)
fft.add_loop("step6", 151, UNROLL_FLATTEN)
fft.add_loop("step6", 164, UNROLL_FLATTEN)
fft.add_loop("step6", 174, UNROLL_FLATTEN)
fft.add_loop("step7", 193)
fft.add_loop("step7", 194, UNROLL_FLATTEN)
fft.add_loop("step8", 216)
fft.add_loop("step8", 217, UNROLL_FLATTEN)
fft.add_loop("step8", 224, UNROLL_FLATTEN)
fft.add_loop("step9", 243)
fft.add_loop("step9", 244, UNROLL_FLATTEN)
fft.add_loop("step10", 266)
fft.add_loop("step10", 267, UNROLL_FLATTEN)
fft.add_loop("step10", 274, UNROLL_FLATTEN)
fft.add_loop("step11", 293)
fft.add_loop("step11", 295, UNROLL_FLATTEN)
fft.add_loop("step11", 304, UNROLL_FLATTEN)

md = Benchmark("md", "md")
md.set_kernels(["md", "md"])
md.add_array("d_force_x", 32, 4, PARTITION_CYCLIC)
md.add_array("d_force_y", 32, 4, PARTITION_CYCLIC)
md.add_array("d_force_z", 32, 4, PARTITION_CYCLIC)
md.add_array("position_x", 32, 4, PARTITION_CYCLIC)
md.add_array("position_y", 32, 4, PARTITION_CYCLIC)
md.add_array("position_z", 32, 4, PARTITION_CYCLIC)
md.add_array("NL", 1024, 4, PARTITION_CYCLIC)
md.add_loop("md", 17)
md.add_loop("md", 25, UNROLL_FLATTEN)

pp_scan = Benchmark("pp_scan", "pp_scan")
pp_scan.set_kernels(["pp_scan", "local_scan", "sum_scan", "last_step_scan"])
pp_scan.add_array("bucket", 2048, 4, PARTITION_CYCLIC)
pp_scan.add_array("bucket2", 2048, 4, PARTITION_CYCLIC)
pp_scan.add_array("sum", 16, 4, PARTITION_CYCLIC)
pp_scan.add_loop("sum_scan", 26)
pp_scan.add_loop("local_scan", 15)
pp_scan.add_loop("local_scan", 16, UNROLL_FLATTEN)
pp_scan.add_loop("last_step_scan", 33)
pp_scan.add_loop("last_step_scan", 34, UNROLL_FLATTEN)

reduction = Benchmark("reduction", "reduction")
reduction.set_kernels(["reduction"])
reduction.add_array("in", 2048, 4, PARTITION_CYCLIC)
reduction.add_loop("reduction", 10)

ss_sort = Benchmark("ss_sort", "ss_sort")
ss_sort.set_kernels(["ss_sort", "init", "hist", "local_scan", "sum_scan",
                     "last_step_scan", "update"])
ss_sort.add_array("a", 2048, 4, PARTITION_CYCLIC)
ss_sort.add_array("b", 2048, 4, PARTITION_CYCLIC)
ss_sort.add_array("bucket", 2048, 4, PARTITION_CYCLIC)
ss_sort.add_array("sum", 128, 4, PARTITION_CYCLIC)
ss_sort.add_loop("init", 52)
ss_sort.add_loop("hist", 61)
ss_sort.add_loop("hist", 63, UNROLL_FLATTEN)
ss_sort.add_loop("local_scan", 17)
ss_sort.add_loop("local_scan", 19, UNROLL_FLATTEN)
ss_sort.add_loop("sum_scan", 30)
ss_sort.add_loop("last_step_scan", 38)
ss_sort.add_loop("last_step_scan", 40, UNROLL_FLATTEN)
ss_sort.add_loop("update", 75)
ss_sort.add_loop("update", 77, UNROLL_FLATTEN)

stencil = Benchmark("stencil", "stencil")
stencil.set_kernels(["stencil"])
stencil.add_array("orig", 1024, 4, PARTITION_CYCLIC)
stencil.add_array("sol", 1024, 4, PARTITION_CYCLIC)
stencil.add_array("filter", 9, 4, PARTITION_CYCLIC)
stencil.add_loop("stencil", 11)
stencil.add_loop("stencil", 12, UNROLL_FLATTEN)

triad = Benchmark("triad", "triad")
triad.set_kernels(["triad"])
triad.add_loop("triad", 10)
triad.add_array("a", 2048, 4, PARTITION_CYCLIC)
triad.add_array("b", 2048, 4, PARTITION_CYCLIC)
triad.add_array("c", 2048, 4, PARTITION_CYCLIC)

SHOC = [bb_gemm, fft, md, pp_scan, reduction, ss_sort, stencil, triad]

bfs_bulk = Benchmark("bfs-bulk", "bfs-bulk")
bfs_bulk.add_array("nodes", 512, 8, PARTITION_CYCLIC)
bfs_bulk.add_array("edges", 4096, 8, PARTITION_CYCLIC)
bfs_bulk.add_array("level", 256, 1, PARTITION_CYCLIC)
bfs_bulk.add_array("level_counts", 10, 8, PARTITION_CYCLIC)
bfs_bulk.add_loop("bfs", 68, 1)
bfs_bulk.add_loop("bfs", 53, 10)
bfs_bulk.add_loop("bfs", 57, 0)

sort_merge = Benchmark("sort-merge", "sort-merge")
sort_merge.add_array("temp", 4096, 4, PARTITION_CYCLIC)
sort_merge.add_array("a", 4096, 4, PARTITION_CYCLIC)
sort_merge.add_loop("mergesort", 70, 1)
sort_merge.add_loop("merge", 41, 2048)
sort_merge.add_loop("merge", 48, 1)
sort_merge.add_loop("mergesort", 69, 1)
sort_merge.add_loop("merge", 37, 2048)

spmv_ellpack = Benchmark("spmv-ellpack", "spmv-ellpack")
spmv_ellpack.add_array("nzval", 4940, 8, PARTITION_CYCLIC)
spmv_ellpack.add_array("cols", 4940, 4, PARTITION_CYCLIC)
spmv_ellpack.add_array("vec", 494, 8, PARTITION_CYCLIC)
spmv_ellpack.add_array("out", 494, 8, PARTITION_CYCLIC)
spmv_ellpack.add_loop("ellpack", 41, 494)
spmv_ellpack.add_loop("ellpack", 43, 10)

bfs_queue = Benchmark("bfs-queue", "bfs-queue")
bfs_queue.add_array("queue", 256, 8, PARTITION_CYCLIC)
bfs_queue.add_array("nodes", 512, 8, PARTITION_CYCLIC)
bfs_queue.add_array("edges", 4096, 8, PARTITION_CYCLIC)
bfs_queue.add_array("level", 256, 1, PARTITION_CYCLIC)
bfs_queue.add_array("level_counts", 10, 8, PARTITION_CYCLIC)
bfs_queue.add_loop("bfs", 63, 1)
bfs_queue.add_loop("bfs", 70, 0)

gemm_blocked = Benchmark("gemm-blocked", "gemm-blocked")
gemm_blocked.add_array("m1", 4096, 4, PARTITION_CYCLIC)
gemm_blocked.add_array("m2", 4096, 4, PARTITION_CYCLIC)
gemm_blocked.add_array("prod", 4096, 4, PARTITION_CYCLIC)
gemm_blocked.add_loop("bbgemm", 46, 8)
gemm_blocked.add_loop("bbgemm", 44, 8)
gemm_blocked.add_loop("bbgemm", 50, 8)
gemm_blocked.add_loop("bbgemm", 43, 8)
gemm_blocked.add_loop("bbgemm", 45, 64)

stencil_stencil3d = Benchmark("stencil-stencil3d", "stencil-stencil3d")
stencil_stencil3d.add_array("orig", 16384, 4, PARTITION_CYCLIC)
stencil_stencil3d.add_array("sol", 16384, 4, PARTITION_CYCLIC)
stencil_stencil3d.add_loop("stencil3d", 43, 30)
stencil_stencil3d.add_loop("stencil3d", 42, 30)
stencil_stencil3d.add_loop("stencil3d", 44, 14)

viterbi_viterbi = Benchmark("viterbi-viterbi", "viterbi-viterbi")
viterbi_viterbi.add_array("Obs", 128, 4, PARTITION_CYCLIC)
viterbi_viterbi.add_array("transMat", 4096, 4, PARTITION_CYCLIC)
viterbi_viterbi.add_array("obsLik", 4096, 4, PARTITION_CYCLIC)
viterbi_viterbi.add_array("v", 4096, 4, PARTITION_CYCLIC)
viterbi_viterbi.add_loop("viterbi", 43, 32)
viterbi_viterbi.add_loop("viterbi", 44, 32)
viterbi_viterbi.add_loop("viterbi", 41, 128)
viterbi_viterbi.add_loop("viterbi", 55, 32)

sort_radix = Benchmark("sort-radix", "sort-radix")
sort_radix.add_array("a", 2048, 4, PARTITION_CYCLIC)
sort_radix.add_array("b", 2048, 4, PARTITION_CYCLIC)
sort_radix.add_array("bucket", 2048, 4, PARTITION_CYCLIC)
sort_radix.add_array("sum", 128, 4, PARTITION_CYCLIC)
sort_radix.add_loop("last_step_scan", 62, 128)
sort_radix.add_loop("local_scan", 42, 16)
sort_radix.add_loop("local_scan", 41, 128)
sort_radix.add_loop("hist", 83, 4)
sort_radix.add_loop("hist", 82, 512)
sort_radix.add_loop("hist", 97, 4)
sort_radix.add_loop("last_step_scan", 63, 16)
sort_radix.add_loop("sum_scan", 53, 128)
sort_radix.add_loop("init", 73, 2048)
sort_radix.add_loop("ss_sort", 110, 1)
sort_radix.add_loop("hist", 96, 512)

kmp_kmp = Benchmark("kmp-kmp", "kmp-kmp")
kmp_kmp.add_array("pattern", 4, 1, PARTITION_CYCLIC)
kmp_kmp.add_array("input", 32411, 1, PARTITION_CYCLIC)
kmp_kmp.add_array("kmpNext", 4, 4, PARTITION_CYCLIC)
kmp_kmp.add_loop("kmp", 61, 1)
kmp_kmp.add_loop("kmp", 60, 32411)
kmp_kmp.add_loop("CPF", 40, 32411)
kmp_kmp.add_loop("CPF", 41, 1)

nw_nw = Benchmark("nw-nw", "nw-nw")
nw_nw.add_array("SEQA", 128, 1, PARTITION_CYCLIC)
nw_nw.add_array("SEQB", 128, 1, PARTITION_CYCLIC)
nw_nw.add_array("allignedA", 256, 1, PARTITION_CYCLIC)
nw_nw.add_array("allignedB", 256, 1, PARTITION_CYCLIC)
nw_nw.add_array("A", 16641, 4, PARTITION_CYCLIC)
nw_nw.add_array("ptr", 16641, 1, PARTITION_CYCLIC)
nw_nw.add_loop("needwun", 54, 128)
nw_nw.add_loop("needwun", 55, 128)
nw_nw.add_loop("needwun", 45, 129)
nw_nw.add_loop("needwun", 99, 128)
nw_nw.add_loop("needwun", 49, 129)

md_grid = Benchmark("md-grid", "md-grid")
md_grid.add_array("n_points", 64, 4, PARTITION_CYCLIC)
md_grid.add_array("d_force", 1920, 8, PARTITION_CYCLIC)
md_grid.add_array("position", 1920, 8, PARTITION_CYCLIC)
md_grid.add_loop("md", 56, 0)
md_grid.add_loop("md", 50, 0)
md_grid.add_loop("md", 62, 0)
md_grid.add_loop("md", 47, 4)
md_grid.add_loop("md", 48, 4)
md_grid.add_loop("md", 46, 4)
md_grid.add_loop("md", 51, 0)
md_grid.add_loop("md", 52, 0)

fft_strided = Benchmark("fft-strided", "fft-strided")
fft_strided.add_array("real", 1024, 8, PARTITION_CYCLIC)
fft_strided.add_array("img", 1024, 8, PARTITION_CYCLIC)
fft_strided.add_array("real_twid", 1024, 8, PARTITION_CYCLIC)
fft_strided.add_array("img_twid", 1024, 8, PARTITION_CYCLIC)
fft_strided.add_loop("fft", 9, 512)
fft_strided.add_loop("fft", 8, 1)

aes_aes = Benchmark("aes-aes", "aes-aes")
aes_aes.add_array("ctx", 96, 1, PARTITION_CYCLIC)
aes_aes.add_array("k", 32, 1, PARTITION_CYCLIC)
aes_aes.add_array("buf", 16, 1, PARTITION_CYCLIC)
aes_aes.add_array("rcon", 1, 1, PARTITION_COMPLETE)
aes_aes.add_array("sbox", 256, 1, PARTITION_CYCLIC)
aes_aes.add_loop("aes_addRoundKey_cpy", 138, 16)
aes_aes.add_loop("aes256_encrypt_ecb", 198, 32)
aes_aes.add_loop("aes_subBytes", 122, 16)
aes_aes.add_loop("aes256_encrypt_ecb", 207, 13)
aes_aes.add_loop("aes_addRoundKey", 130, 16)
aes_aes.add_loop("aes256_encrypt_ecb", 201, 8)

md_knn = Benchmark("md-knn", "md-knn")
md_knn.add_array("d_force_x", 256, 8, PARTITION_CYCLIC)
md_knn.add_array("d_force_y", 256, 8, PARTITION_CYCLIC)
md_knn.add_array("d_force_z", 256, 8, PARTITION_CYCLIC)
md_knn.add_array("position_x", 256, 8, PARTITION_CYCLIC)
md_knn.add_array("position_y", 256, 8, PARTITION_CYCLIC)
md_knn.add_array("position_z", 256, 8, PARTITION_CYCLIC)
md_knn.add_array("NL", 4096, 8, PARTITION_CYCLIC)
md_knn.add_loop("md_kernel", 51, 256)
md_knn.add_loop("md_kernel", 58, 0)

fft_transpose = Benchmark("fft-transpose", "fft-transpose")
fft_transpose.add_array("reversed", 8, 4, PARTITION_COMPLETE)
fft_transpose.add_array("DATA_x", 512, 8, PARTITION_CYCLIC)
fft_transpose.add_array("DATA_y", 512, 8, PARTITION_CYCLIC)
fft_transpose.add_array("data_x", 8, 8, PARTITION_COMPLETE)
fft_transpose.add_array("data_y", 8, 8, PARTITION_COMPLETE)
fft_transpose.add_array("smem", 576, 8, PARTITION_CYCLIC)
fft_transpose.add_array("work_x", 512, 8, PARTITION_CYCLIC)
fft_transpose.add_array("work_y", 512, 8, PARTITION_CYCLIC)
fft_transpose.add_loop("fft1D_512", 392, 64)
fft_transpose.add_loop("twiddles8", 55, 8)
fft_transpose.add_loop("fft1D_512", 154, 64)
fft_transpose.add_loop("fft1D_512", 352, 64)
fft_transpose.add_loop("fft1D_512", 231, 64)
fft_transpose.add_loop("fft1D_512", 246, 64)
fft_transpose.add_loop("fft1D_512", 367, 64)
fft_transpose.add_loop("fft1D_512", 201, 64)
fft_transpose.add_loop("fft1D_512", 336, 64)
fft_transpose.add_loop("fft1D_512", 321, 64)
fft_transpose.add_loop("fft1D_512", 271, 64)
fft_transpose.add_loop("fft1D_512", 215, 64)

stencil_stencil2d = Benchmark("stencil-stencil2d", "stencil-stencil2d")
stencil_stencil2d.add_array("orig", 8192, 4, PARTITION_CYCLIC)
stencil_stencil2d.add_array("sol", 8192, 4, PARTITION_CYCLIC)
stencil_stencil2d.add_array("filter", 9, 4, PARTITION_COMPLETE)
stencil_stencil2d.add_loop("stencil", 39, 62)
stencil_stencil2d.add_loop("stencil", 40, 3)
stencil_stencil2d.add_loop("stencil", 41, 3)
stencil_stencil2d.add_loop("stencil", 38, 126)

spmv_crs = Benchmark("spmv-crs", "spmv-crs")
spmv_crs.add_array("val", 1666, 8, PARTITION_CYCLIC)
spmv_crs.add_array("cols", 1666, 4, PARTITION_CYCLIC)
spmv_crs.add_array("rowDelimiters", 495, 4, PARTITION_CYCLIC)
spmv_crs.add_array("vec", 494, 8, PARTITION_CYCLIC)
spmv_crs.add_array("out", 494, 8, PARTITION_CYCLIC)
spmv_crs.add_loop("spmv", 45, 1)
spmv_crs.add_loop("spmv", 41, 494)

gemm_ncubed = Benchmark("gemm-ncubed", "gemm-ncubed")
gemm_ncubed.add_array("m1", 4096, 4, PARTITION_CYCLIC)
gemm_ncubed.add_array("m2", 4096, 4, PARTITION_CYCLIC)
gemm_ncubed.add_array("prod", 4096, 4, PARTITION_CYCLIC)
gemm_ncubed.add_loop("gemm", 44, 64)
gemm_ncubed.add_loop("gemm", 48, 64)
gemm_ncubed.add_loop("gemm", 45, 64)

MACH = [ bfs_bulk, sort_merge, spmv_ellpack, bfs_queue, gemm_blocked,\
         stencil_stencil3d, viterbi_viterbi, sort_radix, kmp_kmp, \
         nw_nw, md_grid, fft_strided, aes_aes, md_knn, fft_transpose,\
         stencil_stencil2d, spmv_crs, gemm_ncubed]
