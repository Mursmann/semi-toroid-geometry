
---

## 2) `docs/index.html` (GitHub Pages, MathJax-enabled)
This page uses MathJax to render LaTeX in the browser and links to the LaTeX and script files.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Semi-Toroid Geometry — Validation</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link rel="stylesheet" href="https://unpkg.com/water.css@2/out/water.css">
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>
<body>
  <header>
    <h1>Semi-Toroid Geometry — Analytical & Numerical Validation</h1>
    <p>Derivations for metrics, curvature, area/volume and reproducible numerical checks.</p>
  </header>

  <section>
    <h2>Overview</h2>
    <p>This project contains the LaTeX derivations (Chapter 3), a Python validation script and sample results demonstrating convergence of the composite midpoint rule for the semi-torus.</p>
  </section>

  <section>
    <h2>Key formulas</h2>
    <p>Parameterization:</p>
    <p>
      \[
      \mathbf X(u,v) = \big( (R + r\cos v)\cos u,\ (R + r\cos v)\sin u,\ r\sin v \big),
      \quad u\in[0,2\pi],\ v\in[0,\pi].
      \]
    </p>
    <p>Element of surface area:</p>
    <p>\(\;dS = r(R + r\cos v)\,du\,dv\;\)</p>
  </section>

  <section>
    <h2>Files</h2>
    <ul>
      <li><a href="../src/chapter3.tex">LaTeX: chapter3.tex</a></li>
      <li><a href="../src/semi_torus_validation.py">Python: semi_torus_validation.py</a></li>
      <li><a href="../data/semi_torus_convergence.csv">Sample CSV results</a></li>
    </ul>
  </section>

  <section>
    <h2>How to reproduce</h2>
    <pre><code>python src/semi_torus_validation.py
# opens and creates data/semi_torus_convergence.csv</code></pre>
  </section>

  <footer>
    <p>License: MIT — see <a href="../LICENSE">LICENSE</a></p>
  </footer>
</body>
</html>
