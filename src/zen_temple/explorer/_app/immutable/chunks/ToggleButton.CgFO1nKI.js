import{s as B,e as _,a as D,t as S,c as m,b as v,g as T,d as y,f as b,o as r,i as I,h as f,B as k,j as L,n as E,D as M,H as j,G as q}from"./scheduler.Bw2O2KLD.js";import{S as A,i as C}from"./index.Cyrvb228.js";function G(n){let t,e,i,u,s,c=(n[0]?n[1][0]:n[1][1])+"",h,d,o,p;return{c(){t=_("div"),e=_("input"),u=D(),s=_("label"),h=S(c),this.h()},l(a){t=m(a,"DIV",{class:!0});var l=v(t);e=m(l,"INPUT",{type:!0,class:!0,id:!0}),u=T(l),s=m(l,"LABEL",{class:!0,for:!0});var g=v(s);h=y(g,c),g.forEach(b),l.forEach(b),this.h()},h(){r(e,"type","checkbox"),r(e,"class","btn-check"),r(e,"id",i="btn-check-outlined"+n[2]),r(s,"class","btn btn-outline-primary btn-sm"),r(s,"for",d="btn-check-outlined"+n[2]),r(t,"class","toggle")},m(a,l){I(a,t,l),f(t,e),e.checked=n[0],f(t,u),f(t,s),f(s,h),o||(p=[k(e,"change",n[4]),k(e,"change",n[5])],o=!0)},p(a,[l]){l&4&&i!==(i="btn-check-outlined"+a[2])&&r(e,"id",i),l&1&&(e.checked=a[0]),l&3&&c!==(c=(a[0]?a[1][0]:a[1][1])+"")&&L(h,c),l&4&&d!==(d="btn-check-outlined"+a[2])&&r(s,"for",d)},i:E,o:E,d(a){a&&b(t),o=!1,M(p)}}}function H(n,t,e){let{value:i}=t,{texts:u=["on","off"]}=t,s="";j(()=>{e(2,s=Math.random().toString(16).slice(2))});const c=q();function h(){i=this.checked,e(0,i)}const d=()=>{c("change")};return n.$$set=o=>{"value"in o&&e(0,i=o.value),"texts"in o&&e(1,u=o.texts)},[i,u,s,c,h,d]}class U extends A{constructor(t){super(),C(this,t,H,G,B,{value:0,texts:1})}}export{U as T};
