# src/semi_torus_validation.py
import numpy as np
import pandas as pd
import os

def numeric_area_volume(R, r, N, M):
    du = 2*np.pi / N
    dv = np.pi / M
    ui = (np.arange(N)+0.5)*du
    vj = (np.arange(M)+0.5)*dv
    U, V = np.meshgrid(ui, vj, indexing='ij')
    dS = r * (R + r * np.cos(V))
    A_num = np.sum(dS) * du * dv
    dV = (R + r * np.cos(V)) * r**2
    V_num = np.sum(dV) * du * dv
    return A_num, V_num

def run_convergence():
    R = 2.0
    r = 0.5
    A_analytic = 2 * np.pi**2 * R * r
    V_analytic = np.pi**2 * R * r**2

    Ns = [10, 20, 40, 80, 160, 320]
    rows = []
    for N in Ns:
        M = max(1, N//2)
        A_num, V_num = numeric_area_volume(R, r, N, M)
        rows.append({
            'N': N, 'M': M,
            'A_num': float(A_num), 'A_err_abs': float(abs(A_num - A_analytic)),
            'A_err_rel': float(abs(A_num - A_analytic)/A_analytic),
            'V_num': float(V_num), 'V_err_abs': float(abs(V_num - V_analytic)),
            'V_err_rel': float(abs(V_num - V_analytic)/V_analytic)
        })
    df = pd.DataFrame(rows)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/semi_torus_convergence.csv', index=False)
    print(df.to_string(index=False))

if __name__ == '__main__':
    run_convergence()
