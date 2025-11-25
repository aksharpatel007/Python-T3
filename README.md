# 📘 Bootstrap Cheatsheet — README
A clean and developer‑friendly **Bootstrap 5 Cheatsheet** with installation steps, layout guides, utilities, and examples. Use this README directly in your GitHub repository.

---

## 🚀 Overview
This cheatsheet provides a quick reference for commonly used **Bootstrap utilities, components, and layout rules**. It's ideal for beginners and professionals needing a fast lookup while building responsive websites.

---

## 📦 Installation
### **Using CDN**
```html
<!-- CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
```

### **Using NPM**
```bash
npm install bootstrap
```

---

## 🎨 Colors
Common Bootstrap text & background color classes:
```
text-primary    bg-primary
text-secondary  bg-secondary
text-success    bg-success
text-danger     bg-danger
text-warning    bg-warning
text-info       bg-info
text-light      bg-light
text-dark       bg-dark
```

---

## 📐 Spacing Utilities
Use `m` for margin, `p` for padding.
```
m-0  m-1  m-2  m-3  m-4  m-5
p-0  p-1  p-2  p-3  p-4  p-5
mt-3 mb-3 ms-3 me-3
pt-3 pb-3 ps-3 pe-3
mx-auto my-4 px-4 py-2
```

---

## 📏 Display Utilities
```
d-none
d-block
d-inline
d-inline-block
d-flex
d-grid
d-md-block
d-lg-none
```

---

## ✍️ Typography
```
h1-h6     Text headings
lead      Larger subtitle text
fw-bold   Bold text
fw-light  Light text
text-uppercase
text-center
```

---

## 🧱 Grid System
### **Basic Layout**
```html
<div class="container">
  <div class="row">
    <div class="col">Column 1</div>
    <div class="col">Column 2</div>
    <div class="col">Column 3</div>
  </div>
</div>
```

### **Column Sizes**
```
col-4       (mobile full width)
col-sm-6
col-md-4
col-lg-3
col-xl-2
```

### **Grid Alignment**
```
justify-content-center
align-items-center
g-3 (grid gap)
```

---

## 🎛 Buttons
```html
btn btn-primary
btn btn-outline-success
btn-lg
btn-sm
w-100
```

---

## 🧩 Forms
```html
<form>
  <input class="form-control" placeholder="Enter text">
  <select class="form-select mt-2"></select>
  <button class="btn btn-primary mt-3">Submit</button>
</form>
```

---

## 🟦 Cards
```html
<div class="card" style="width: 18rem;">
  <img src="img.jpg" class="card-img-top">
  <div class="card-body">
    <h5 class="card-title">Card Title</h5>
    <p class="card-text">Description text goes here.</p>
    <button class="btn btn-dark">Read More</button>
  </div>
</div>
```

---

## ⚙️ Flex Utilities
```
d-flex
flex-row
flex-column
justify-content-between
align-items-center
gap-3
```

---

## 🧭 Navbar Example
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Brand</a>

    <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#menu">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="menu">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#">About</a></li>
      </ul>
    </div>
  </div>
</nav>
```

---

## 🔗 Additional Resources
- Official Docs: https://getbootstrap.com
- Bootstrap Icons: https://icons.getbootstrap.com

---

## ⭐ Contributing
Feel free to fork this repository and submit improvements, examples, or additional UI components.

---

### 💙 Enjoy building with Bootstrap!


---

# 🧾 Complete Bootstrap 5 Classes & Components Reference
This extended section includes **almost all commonly used Bootstrap classes** categorized for quick lookup.

---

## 🎨 Colors (Text & Background)
```
text-primary      bg-primary
text-secondary    bg-secondary
text-success      bg-success
text-danger       bg-danger
text-warning      bg-warning
text-info         bg-info
text-light        bg-light
text-dark         bg-dark
text-muted        bg-muted
text-white        bg-white
text-black        bg-black
```

---

## 🔤 Typography Classes
```
h1 – h6
fs-1 – fs-6 (font sizes)
fst-italic
fst-normal
fw-bold
fw-semibold
fw-normal
fw-light
text-start
text-center
text-end
text-uppercase
text-lowercase
text-capitalize
lh-1 lh-sm lh-base lh-lg lh-xl (line height)
```

---

## 📐 Spacing Utilities
### **Margin (m), Padding (p)**
```
0 1 2 3 4 5 auto
m, mt, mb, ms, me, mx, my
p, pt, pb, ps, pe, px, py
```
Example:
```
mt-3   mx-auto   p-4   px-2
```

---

## 📏 Display Utilities
```
d-none
d-inline
d-inline-block
d-block
d-flex
d-inline-flex
d-grid
d-table
d-lg-none
d-md-block
```

---

## 🧱 Flexbox Utilities
```
flex-row
flex-column
flex-row-reverse
flex-column-reverse
flex-wrap
flex-nowrap
justify-content-start
justify-content-end
justify-content-center
justify-content-between
justify-content-around
align-items-start
align-items-end
align-items-center
gap-1 gap-2 gap-3 gap-4 gap-5
```

---

## 🟦 Grid System Complete
```
.container .container-fluid .container-sm .container-lg
.row
.col .col-auto
col-1 – col-12
col-sm-* col-md-* col-lg-* col-xl-* col-xxl-*
offset-* offset-sm-* offset-md-*
order-1 order-2 order-3
```

---

## 🔲 Borders
```
border
border-0
border-top
border-bottom
border-start
border-end
border-primary border-success border-danger
rounded
rounded-0
rounded-circle
rounded-pill
```

---

## 📦 Sizing
```
w-25  w-50  w-75  w-100  w-auto
h-25  h-50  h-75  h-100  h-auto
vw-100  vh-100
min-vw-100  min-vh-100
```

---

## 💠 Position Utilities
```
position-static
position-relative
position-absolute
position-fixed
position-sticky
top-0 bottom-0 start-0 end-0
translate-middle
```

---

## 🌫 Shadows
```
shadow-none
shadow-sm
shadow
shadow-lg
```

---

# 🧩 Complete Bootstrap Components
Below is the full list of key Bootstrap components.

---

## 🔔 Alerts
```
alert alert-primary
alert-success
alert-danger
alert-warning
alert-info
alert-light
alert-dark
```

---

## 🎛 Badges
```
badge bg-primary
badge rounded-pill
```

---

## 🔳 Buttons
```
btn btn-primary
btn-secondary btn-success btn-danger
btn-outline-primary
btn-lg btn-sm btn-block
```

---

## 🔘 Button Group
```
btn-group
btn-group-vertical
```

---

## 📚 Cards
```
card
card-body
card-title
card-text
card-header
card-footer
card-img-top
```

---

## 📝 Forms
```
form-control
form-select
form-label
form-check
form-check-input
form-check-label
input-group
input-group-text
```

---

## 🚥 Nav & Navbar
```
navbar navbar-light navbar-dark
navbar-expand
navbar-brand
navbar-nav
nav-item
nav-link
```

---

## 📂 List Group
```
list-group
list-group-item
list-group-item-action
list-group-numbered
list-group-flush
```

---

## 📌 Modal
```
modal
modal-dialog
modal-content
modal-header
modal-body
modal-footer
```

---

## 🧭 Pagination
```
pagination
page-item
page-link
```

---

## 📊 Progress Bar
```
progress
progress-bar
progress-bar-striped
progress-bar-animated
```

---

## 🔄 Spinner
```
spinner-border
spinner-grow
```

---

## ⚡ Toast
```
toast
toast-header
toast-body
```

---

## 🧱 Accordion
```
accordion
accordion-item
accordion-header
accordion-button
accordion-collapse
```

---

## 🔲 Tabs
```
nav nav-tabs
nav nav-pills
```

---

## 🏗 Utilities
```
overflow-auto
overflow-hidden
ratio ratio-16x9 ratio-4x3 ratio-1x1
opacity-25 opacity-50 opacity-75 opacity-100
z-0 z-1 z-3 z-5
```

---

# ✅ End of Full Bootstrap 5 Reference
If you want a **PDF version**, **dark theme version**, or **print-friendly cheatsheet**, tell me!
