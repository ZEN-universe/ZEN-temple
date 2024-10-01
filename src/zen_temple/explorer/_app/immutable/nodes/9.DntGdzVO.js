import{s as _t,r as A,e as D,a as B,c as I,m as te,g as R,b as M,f as k,o as H,v as me,i as G,h as y,w as Y,y as Ae,z as we,A as ye,B as Be,C as Re,t as Ye,d as Fe,D as De,j as Ge,E as He,n as Z}from"../chunks/scheduler.Bjr9RZaN.js";import{S as ct,i as ft,b as F,c as re,d as ae,m as _e,t as q,a as P,e as pe,f as ce,g as he}from"../chunks/index.NoFf4Nre.js";import{e as Ie}from"../chunks/each.D6YF6ztN.js";import{S as ut,g as dt,f as pt,B as ht}from"../chunks/utils.D6vKzzmz.js";import{R as Ve,A as Te}from"../chunks/Radio.D-A72FRT.js";function Le(t,e,l){const a=t.slice();return a[64]=e[l],a}function Se(t,e,l){const a=t.slice();return a[67]=e[l][0],a[68]=e[l][1],a}function Me(t){let e,l,a='<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">Variable Selection</button>',r,u,o,s,c,v,C,n,_,g,i=Ie(Object.entries(t[5])),m=[];for(let h=0;h<i.length;h+=1)m[h]=Oe(Se(t,i,h));let E=t[5]&&t[9]&&t[5][t[9]]!=null&&ze(t),b=t[9]!=null&&qe(t);return{c(){e=D("div"),l=D("h2"),l.innerHTML=a,r=B(),u=D("div"),o=D("div"),s=D("select");for(let h=0;h<m.length;h+=1)m[h].c();v=B(),E&&E.c(),C=B(),b&&b.c(),this.h()},l(h){e=I(h,"DIV",{class:!0});var L=M(e);l=I(L,"H2",{class:!0,"data-svelte-h":!0}),te(l)!=="svelte-1b944yg"&&(l.innerHTML=a),r=R(L),u=I(L,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var w=M(u);o=I(w,"DIV",{class:!0});var j=M(o);s=I(j,"SELECT",{});var W=M(s);for(let O=0;O<m.length;O+=1)m[O].l(W);W.forEach(k),v=R(j),E&&E.l(j),C=R(j),b&&b.l(j),j.forEach(k),w.forEach(k),L.forEach(k),this.h()},h(){H(l,"class","accordion-header"),s.disabled=c=t[18]||t[19],t[9]===void 0&&Ae(()=>t[33].call(s)),H(o,"class","accordion-body"),H(u,"id","collapseTwo"),H(u,"class","accordion-collapse collapse"),H(u,"data-bs-parent","#accordionExample"),H(e,"class","accordion-item")},m(h,L){G(h,e,L),y(e,l),y(e,r),y(e,u),y(u,o),y(o,s);for(let w=0;w<m.length;w+=1)m[w]&&m[w].m(s,null);we(s,t[9],!0),y(o,v),E&&E.m(o,null),y(o,C),b&&b.m(o,null),n=!0,_||(g=[ye(s,"change",t[33]),ye(s,"change",t[34])],_=!0)},p(h,L){if(L[0]&32){i=Ie(Object.entries(h[5]));let w;for(w=0;w<i.length;w+=1){const j=Se(h,i,w);m[w]?m[w].p(j,L):(m[w]=Oe(j),m[w].c(),m[w].m(s,null))}for(;w<m.length;w+=1)m[w].d(1);m.length=i.length}(!n||L[0]&786432&&c!==(c=h[18]||h[19]))&&(s.disabled=c),L[0]&544&&we(s,h[9]),h[5]&&h[9]&&h[5][h[9]]!=null?E?(E.p(h,L),L[0]&544&&q(E,1)):(E=ze(h),E.c(),q(E,1),E.m(o,C)):E&&(he(),P(E,1,1,()=>{E=null}),pe()),h[9]!=null?b?b.p(h,L):(b=qe(h),b.c(),b.m(o,null)):b&&(b.d(1),b=null)},i(h){n||(q(E),n=!0)},o(h){P(E),n=!1},d(h){h&&k(e),Be(m,h),E&&E.d(),b&&b.d(),_=!1,Re(g)}}}function Oe(t){let e,l=t[67]+"",a,r,u;return{c(){e=D("option"),a=Ye(l),r=B(),this.h()},l(o){e=I(o,"OPTION",{});var s=M(e);a=Fe(s,l),r=R(s),s.forEach(k),this.h()},h(){e.__value=u=t[67],De(e,e.__value)},m(o,s){G(o,e,s),y(e,a),y(e,r)},p(o,s){s[0]&32&&l!==(l=o[67]+"")&&Ge(a,l),s[0]&32&&u!==(u=o[67])&&(e.__value=u,De(e,e.__value))},d(o){o&&k(e)}}}function ze(t){let e,l,a,r;function u(c){t[35](c)}function o(c){t[36](c)}let s={enabled:!t[18]&&!t[19]};return t[5][t[9]]!==void 0&&(s.options=t[5][t[9]]),t[14]!==void 0&&(s.selected_option=t[14]),e=new Ve({props:s}),A.push(()=>F(e,"options",u)),A.push(()=>F(e,"selected_option",o)),e.$on("selection-changed",t[37]),{c(){re(e.$$.fragment)},l(c){ae(e.$$.fragment,c)},m(c,v){_e(e,c,v),r=!0},p(c,v){const C={};v[0]&786432&&(C.enabled=!c[18]&&!c[19]),!l&&v[0]&544&&(l=!0,C.options=c[5][c[9]],Y(()=>l=!1)),!a&&v[0]&16384&&(a=!0,C.selected_option=c[14],Y(()=>a=!1)),e.$set(C)},i(c){r||(q(e.$$.fragment,c),r=!0)},o(c){P(e.$$.fragment,c),r=!1},d(c){ce(e,c)}}}function qe(t){let e,l,a,r="Carrier",u,o,s,c,v,C=Ie(t[0]),n=[];for(let _=0;_<C.length;_+=1)n[_]=je(Le(t,C,_));return{c(){e=D("div"),l=D("div"),a=D("h3"),a.textContent=r,u=B(),o=D("select");for(let _=0;_<n.length;_+=1)n[_].c();this.h()},l(_){e=I(_,"DIV",{class:!0});var g=M(e);l=I(g,"DIV",{class:!0});var i=M(l);a=I(i,"H3",{"data-svelte-h":!0}),te(a)!=="svelte-xc22hm"&&(a.textContent=r),u=R(i),o=I(i,"SELECT",{});var m=M(o);for(let E=0;E<n.length;E+=1)n[E].l(m);m.forEach(k),i.forEach(k),g.forEach(k),this.h()},h(){o.disabled=s=t[18]||t[19],t[10]===void 0&&Ae(()=>t[38].call(o)),H(l,"class","col"),H(e,"class","row")},m(_,g){G(_,e,g),y(e,l),y(l,a),y(l,u),y(l,o);for(let i=0;i<n.length;i+=1)n[i]&&n[i].m(o,null);we(o,t[10],!0),c||(v=[ye(o,"change",t[38]),ye(o,"change",t[39])],c=!0)},p(_,g){if(g[0]&1){C=Ie(_[0]);let i;for(i=0;i<C.length;i+=1){const m=Le(_,C,i);n[i]?n[i].p(m,g):(n[i]=je(m),n[i].c(),n[i].m(o,null))}for(;i<n.length;i+=1)n[i].d(1);n.length=C.length}g[0]&786432&&s!==(s=_[18]||_[19])&&(o.disabled=s),g[0]&1025&&we(o,_[10])},d(_){_&&k(e),Be(n,_),c=!1,Re(v)}}}function je(t){let e,l=t[64]+"",a,r,u;return{c(){e=D("option"),a=Ye(l),r=B(),this.h()},l(o){e=I(o,"OPTION",{});var s=M(e);a=Fe(s,l),r=R(s),s.forEach(k),this.h()},h(){e.__value=u=t[64],De(e,e.__value)},m(o,s){G(o,e,s),y(e,a),y(e,r)},p(o,s){s[0]&1&&l!==(l=o[64]+"")&&Ge(a,l),s[0]&1&&u!==(u=o[64])&&(e.__value=u,De(e,e.__value))},d(o){o&&k(e)}}}function Ne(t){let e,l,a='<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">Data Selection</button>',r,u,o,s,c,v,C,n="Normalisation",_,g,i,m,E,b,h,L,w,j="Year",W,O,X,U,z,V=t[9]!="import_export"&&Pe(t);function $(p){t[43](p)}function ue(p){t[44](p)}let fe={enabled:!t[18]&&!t[19]};t[16]!==void 0&&(fe.options=t[16]),t[17]!==void 0&&(fe.selected_option=t[17]),g=new Ve({props:fe}),A.push(()=>F(g,"options",$)),A.push(()=>F(g,"selected_option",ue)),g.$on("selection-changed",t[45]);const oe=[mt,gt],x=[];function ne(p,N){return p[20]=="technology"?0:1}b=ne(t),h=x[b]=oe[b](t);function ge(p){t[52](p)}function le(p){t[53](p)}let T={enabled:!t[18]&&!t[19]};return t[15]!==void 0&&(T.selected_elements=t[15]),t[4]!==void 0&&(T.elements=t[4]),O=new Te({props:T}),A.push(()=>F(O,"selected_elements",ge)),A.push(()=>F(O,"elements",le)),O.$on("selection-changed",t[54]),{c(){e=D("div"),l=D("h2"),l.innerHTML=a,r=B(),u=D("div"),o=D("div"),s=D("div"),V&&V.c(),c=B(),v=D("div"),C=D("h3"),C.textContent=n,_=B(),re(g.$$.fragment),E=B(),h.c(),L=B(),w=D("h3"),w.textContent=j,W=B(),re(O.$$.fragment),this.h()},l(p){e=I(p,"DIV",{class:!0});var N=M(e);l=I(N,"H2",{class:!0,"data-svelte-h":!0}),te(l)!=="svelte-hz94lo"&&(l.innerHTML=a),r=R(N),u=I(N,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var J=M(u);o=I(J,"DIV",{class:!0});var Q=M(o);s=I(Q,"DIV",{class:!0});var f=M(s);V&&V.l(f),c=R(f),v=I(f,"DIV",{class:!0});var S=M(v);C=I(S,"H3",{"data-svelte-h":!0}),te(C)!=="svelte-1273uzu"&&(C.textContent=n),_=R(S),ae(g.$$.fragment,S),S.forEach(k),f.forEach(k),E=R(Q),h.l(Q),L=R(Q),w=I(Q,"H3",{"data-svelte-h":!0}),te(w)!=="svelte-r9e7qt"&&(w.textContent=j),W=R(Q),ae(O.$$.fragment,Q),Q.forEach(k),J.forEach(k),N.forEach(k),this.h()},h(){H(l,"class","accordion-header"),H(v,"class","col-6"),H(s,"class","row"),H(o,"class","accordion-body"),H(u,"id","collapseThree"),H(u,"class","accordion-collapse collapse"),H(u,"data-bs-parent","#accordionExample"),H(e,"class","accordion-item")},m(p,N){G(p,e,N),y(e,l),y(e,r),y(e,u),y(u,o),y(o,s),V&&V.m(s,null),y(s,c),y(s,v),y(v,C),y(v,_),_e(g,v,null),y(o,E),x[b].m(o,null),y(o,L),y(o,w),y(o,W),_e(O,o,null),z=!0},p(p,N){p[9]!="import_export"?V?(V.p(p,N),N[0]&512&&q(V,1)):(V=Pe(p),V.c(),q(V,1),V.m(s,c)):V&&(he(),P(V,1,1,()=>{V=null}),pe());const J={};N[0]&786432&&(J.enabled=!p[18]&&!p[19]),!i&&N[0]&65536&&(i=!0,J.options=p[16],Y(()=>i=!1)),!m&&N[0]&131072&&(m=!0,J.selected_option=p[17],Y(()=>m=!1)),g.$set(J);let Q=b;b=ne(p),b===Q?x[b].p(p,N):(he(),P(x[Q],1,1,()=>{x[Q]=null}),pe(),h=x[b],h?h.p(p,N):(h=x[b]=oe[b](p),h.c()),q(h,1),h.m(o,L));const f={};N[0]&786432&&(f.enabled=!p[18]&&!p[19]),!X&&N[0]&32768&&(X=!0,f.selected_elements=p[15],Y(()=>X=!1)),!U&&N[0]&16&&(U=!0,f.elements=p[4],Y(()=>U=!1)),O.$set(f)},i(p){z||(q(V),q(g.$$.fragment,p),q(h),q(O.$$.fragment,p),z=!0)},o(p){P(V),P(g.$$.fragment,p),P(h),P(O.$$.fragment,p),z=!1},d(p){p&&k(e),V&&V.d(),ce(g),x[b].d(),ce(O)}}}function Pe(t){let e,l,a="Aggregation",r,u,o,s,c;function v(_){t[40](_)}function C(_){t[41](_)}let n={enabled:!t[18]&&!t[19]};return t[6]!==void 0&&(n.options=t[6]),t[20]!==void 0&&(n.selected_option=t[20]),u=new Ve({props:n}),A.push(()=>F(u,"options",v)),A.push(()=>F(u,"selected_option",C)),u.$on("selection-changed",t[42]),{c(){e=D("div"),l=D("h3"),l.textContent=a,r=B(),re(u.$$.fragment),this.h()},l(_){e=I(_,"DIV",{class:!0});var g=M(e);l=I(g,"H3",{"data-svelte-h":!0}),te(l)!=="svelte-126hufg"&&(l.textContent=a),r=R(g),ae(u.$$.fragment,g),g.forEach(k),this.h()},h(){H(e,"class","col-6")},m(_,g){G(_,e,g),y(e,l),y(e,r),_e(u,e,null),c=!0},p(_,g){const i={};g[0]&786432&&(i.enabled=!_[18]&&!_[19]),!o&&g[0]&64&&(o=!0,i.options=_[6],Y(()=>o=!1)),!s&&g[0]&1048576&&(s=!0,i.selected_option=_[20],Y(()=>s=!1)),u.$set(i)},i(_){c||(q(u.$$.fragment,_),c=!0)},o(_){P(u.$$.fragment,_),c=!1},d(_){_&&k(e),ce(u)}}}function gt(t){let e,l="Node",a,r,u,o,s;function c(n){t[49](n)}function v(n){t[50](n)}let C={enabled:!t[18]&&!t[19]};return t[13]!==void 0&&(C.selected_elements=t[13]),t[3]!==void 0&&(C.elements=t[3]),r=new Te({props:C}),A.push(()=>F(r,"selected_elements",c)),A.push(()=>F(r,"elements",v)),r.$on("selection-changed",t[51]),{c(){e=D("h3"),e.textContent=l,a=B(),re(r.$$.fragment)},l(n){e=I(n,"H3",{"data-svelte-h":!0}),te(e)!=="svelte-ocjo5w"&&(e.textContent=l),a=R(n),ae(r.$$.fragment,n)},m(n,_){G(n,e,_),G(n,a,_),_e(r,n,_),s=!0},p(n,_){const g={};_[0]&786432&&(g.enabled=!n[18]&&!n[19]),!u&&_[0]&8192&&(u=!0,g.selected_elements=n[13],Y(()=>u=!1)),!o&&_[0]&8&&(o=!0,g.elements=n[3],Y(()=>o=!1)),r.$set(g)},i(n){s||(q(r.$$.fragment,n),s=!0)},o(n){P(r.$$.fragment,n),s=!1},d(n){n&&(k(e),k(a)),ce(r,n)}}}function mt(t){let e,l="Technology",a,r,u,o,s;function c(n){t[46](n)}function v(n){t[47](n)}let C={enabled:!t[18]&&!t[19]};return t[12]!==void 0&&(C.selected_elements=t[12]),t[11]!==void 0&&(C.elements=t[11]),r=new Te({props:C}),A.push(()=>F(r,"selected_elements",c)),A.push(()=>F(r,"elements",v)),r.$on("selection-changed",t[48]),{c(){e=D("h3"),e.textContent=l,a=B(),re(r.$$.fragment)},l(n){e=I(n,"H3",{"data-svelte-h":!0}),te(e)!=="svelte-q7cxxi"&&(e.textContent=l),a=R(n),ae(r.$$.fragment,n)},m(n,_){G(n,e,_),G(n,a,_),_e(r,n,_),s=!0},p(n,_){const g={};_[0]&786432&&(g.enabled=!n[18]&&!n[19]),!u&&_[0]&4096&&(u=!0,g.selected_elements=n[12],Y(()=>u=!1)),!o&&_[0]&2048&&(o=!0,g.elements=n[11],Y(()=>o=!1)),r.$set(g)},i(n){s||(q(r.$$.fragment,n),s=!0)},o(n){P(r.$$.fragment,n),s=!1},d(n){n&&(k(e),k(a)),ce(r,n)}}}function bt(t){let e,l,a,r;function u(c){t[55](c)}function o(c){t[56](c)}let s={};return t[21]!==void 0&&(s.config=t[21]),t[8].detail.system.reference_year!==void 0&&(s.year_offset=t[8].detail.system.reference_year),e=new ht({props:s}),A.push(()=>F(e,"config",u)),A.push(()=>F(e,"year_offset",o)),{c(){re(e.$$.fragment)},l(c){ae(e.$$.fragment,c)},m(c,v){_e(e,c,v),r=!0},p(c,v){const C={};!l&&v[0]&2097152&&(l=!0,C.config=c[21],Y(()=>l=!1)),!a&&v[0]&256&&(a=!0,C.year_offset=c[8].detail.system.reference_year,Y(()=>a=!1)),e.$set(C)},i(c){r||(q(e.$$.fragment,c),r=!0)},o(c){P(e.$$.fragment,c),r=!1},d(c){ce(e,c)}}}function vt(t){let e,l="No data with this selection.";return{c(){e=D("div"),e.textContent=l,this.h()},l(a){e=I(a,"DIV",{class:!0,"data-svelte-h":!0}),te(e)!=="svelte-1doxial"&&(e.textContent=l),this.h()},h(){H(e,"class","text-center")},m(a,r){G(a,e,r)},p:Z,i:Z,o:Z,d(a){a&&k(e)}}}function kt(t){let e,l="No technologies with this selection.";return{c(){e=D("div"),e.textContent=l,this.h()},l(a){e=I(a,"DIV",{class:!0,"data-svelte-h":!0}),te(e)!=="svelte-1ontq7"&&(e.textContent=l),this.h()},h(){H(e,"class","text-center")},m(a,r){G(a,e,r)},p:Z,i:Z,o:Z,d(a){a&&k(e)}}}function Ct(t){let e;return{c(){e=D("div")},l(l){e=I(l,"DIV",{}),M(e).forEach(k)},m(l,a){G(l,e,a)},p:Z,i:Z,o:Z,d(l){l&&k(e)}}}function Et(t){let e;return{c(){e=D("div")},l(l){e=I(l,"DIV",{}),M(e).forEach(k)},m(l,a){G(l,e,a)},p:Z,i:Z,o:Z,d(l){l&&k(e)}}}function wt(t){let e,l='<div class="spinner-border center" role="status"><span class="visually-hidden">Loading...</span></div>';return{c(){e=D("div"),e.innerHTML=l,this.h()},l(a){e=I(a,"DIV",{class:!0,"data-svelte-h":!0}),te(e)!=="svelte-1a5ljpq"&&(e.innerHTML=l),this.h()},h(){H(e,"class","text-center")},m(a,r){G(a,e,r)},p:Z,i:Z,o:Z,d(a){a&&k(e)}}}function yt(t){let e,l='<div class="col"><h2>Production</h2></div>',a,r,u,o,s,c,v,C='<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">Solution Selection</button>',n,_,g,i,m,E,b,h,L,w,j,W,O,X,U,z,V,$;function ue(f){t[27](f)}function fe(f){t[28](f)}function oe(f){t[29](f)}function x(f){t[30](f)}function ne(f){t[31](f)}function ge(f){t[32](f)}let le={enabled:!t[18]&&!t[19]};t[0]!==void 0&&(le.carriers=t[0]),t[1]!==void 0&&(le.nodes=t[1]),t[4]!==void 0&&(le.years=t[4]),t[8]!==void 0&&(le.selected_solution=t[8]),t[2]!==void 0&&(le.edges=t[2]),t[18]!==void 0&&(le.loading=t[18]),i=new ut({props:le}),A.push(()=>F(i,"carriers",ue)),A.push(()=>F(i,"nodes",fe)),A.push(()=>F(i,"years",oe)),A.push(()=>F(i,"selected_solution",x)),A.push(()=>F(i,"edges",ne)),A.push(()=>F(i,"loading",ge)),i.$on("solution_selected",t[23]);let T=!t[18]&&t[8]&&Me(t),p=!t[19]&&t[10]&&(t[11].length>0||t[9]=="import_export")&&Ne(t);const N=[wt,Et,Ct,kt,vt,bt],J=[];function Q(f,S){return f[18]||f[19]?0:f[8]==null?1:f[7]==null?2:f[11].length==0&&f[9]!="import_export"?3:f[7].length==0?4:5}return z=Q(t),V=J[z]=N[z](t),{c(){e=D("div"),e.innerHTML=l,a=B(),r=D("div"),u=D("div"),o=D("div"),s=D("div"),c=D("div"),v=D("h2"),v.innerHTML=C,n=B(),_=D("div"),g=D("div"),re(i.$$.fragment),j=B(),T&&T.c(),W=B(),p&&p.c(),O=B(),X=D("div"),U=D("div"),V.c(),this.h()},l(f){e=I(f,"DIV",{class:!0,"data-svelte-h":!0}),te(e)!=="svelte-1ow2g6f"&&(e.innerHTML=l),a=R(f),r=I(f,"DIV",{class:!0});var S=M(r);u=I(S,"DIV",{class:!0,style:!0});var ee=M(u);o=I(ee,"DIV",{class:!0,style:!0});var se=M(o);s=I(se,"DIV",{class:!0,id:!0});var ie=M(s);c=I(ie,"DIV",{class:!0});var de=M(c);v=I(de,"H2",{class:!0,"data-svelte-h":!0}),te(v)!=="svelte-64kjki"&&(v.innerHTML=C),n=R(de),_=I(de,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var be=M(_);g=I(be,"DIV",{class:!0});var ve=M(g);ae(i.$$.fragment,ve),ve.forEach(k),be.forEach(k),de.forEach(k),j=R(ie),T&&T.l(ie),W=R(ie),p&&p.l(ie),ie.forEach(k),se.forEach(k),ee.forEach(k),S.forEach(k),O=R(f),X=I(f,"DIV",{class:!0});var ke=M(X);U=I(ke,"DIV",{class:!0,style:!0});var Ce=M(U);V.l(Ce),Ce.forEach(k),ke.forEach(k),this.h()},h(){H(e,"class","row"),H(v,"class","accordion-header"),H(g,"class","accordion-body"),H(_,"id","collapseOne"),H(_,"class","accordion-collapse collapse show"),H(_,"data-bs-parent","#accordionExample"),H(c,"class","accordion-item solution-selection"),H(s,"class","accordion"),H(s,"id","accordionExample"),H(o,"class","filters"),me(o,"position","absolute"),me(o,"width","100%"),H(u,"class","col position-relative"),me(u,"z-index","1"),me(u,"position","relative"),H(r,"class","row"),H(U,"class","col"),me(U,"margin-top","400px"),H(X,"class","row")},m(f,S){G(f,e,S),G(f,a,S),G(f,r,S),y(r,u),y(u,o),y(o,s),y(s,c),y(c,v),y(c,n),y(c,_),y(_,g),_e(i,g,null),y(s,j),T&&T.m(s,null),y(s,W),p&&p.m(s,null),G(f,O,S),G(f,X,S),y(X,U),J[z].m(U,null),$=!0},p(f,S){const ee={};S[0]&786432&&(ee.enabled=!f[18]&&!f[19]),!m&&S[0]&1&&(m=!0,ee.carriers=f[0],Y(()=>m=!1)),!E&&S[0]&2&&(E=!0,ee.nodes=f[1],Y(()=>E=!1)),!b&&S[0]&16&&(b=!0,ee.years=f[4],Y(()=>b=!1)),!h&&S[0]&256&&(h=!0,ee.selected_solution=f[8],Y(()=>h=!1)),!L&&S[0]&4&&(L=!0,ee.edges=f[2],Y(()=>L=!1)),!w&&S[0]&262144&&(w=!0,ee.loading=f[18],Y(()=>w=!1)),i.$set(ee),!f[18]&&f[8]?T?(T.p(f,S),S[0]&262400&&q(T,1)):(T=Me(f),T.c(),q(T,1),T.m(s,W)):T&&(he(),P(T,1,1,()=>{T=null}),pe()),!f[19]&&f[10]&&(f[11].length>0||f[9]=="import_export")?p?(p.p(f,S),S[0]&527872&&q(p,1)):(p=Ne(f),p.c(),q(p,1),p.m(s,null)):p&&(he(),P(p,1,1,()=>{p=null}),pe());let se=z;z=Q(f),z===se?J[z].p(f,S):(he(),P(J[se],1,1,()=>{J[se]=null}),pe(),V=J[z],V?V.p(f,S):(V=J[z]=N[z](f),V.c()),q(V,1),V.m(U,null))},i(f){$||(q(i.$$.fragment,f),q(T),q(p),q(V),$=!0)},o(f){P(i.$$.fragment,f),P(T),P(p),P(V),$=!1},d(f){f&&(k(e),k(a),k(r),k(O),k(X)),ce(i),T&&T.d(),p&&p.d(),J[z].d()}}}function Dt(t,e,l){let a,r=[],u=[],o=[],s=[],c=[],v={conversion:["input","output"],storage:["charge","discharge"],transport:null,import_export:["import","export"]},C=["technology","node"],n=null,_=null,g="",i=null,m=null,E=null,b=[],h=[],L=[],w=null,j=[],W=["not_normalized","normalized"],O="not_normalized",X=!1,U=!1,z="node",$={type:"bar",data:{datasets:[]},options:{responsive:!0,scales:{x:{stacked:!0,title:{display:!0,text:"Year"}},y:{stacked:!0,title:{display:!0,text:m+" ["+g+"]"}}}}};function ue(){l(15,j=c),l(13,L=u),l(12,h=b)}function fe(){switch(m){case"conversion":return"flow_conversion_"+w;case"storage":return"flow_storage_"+w;case"transport":return"flow_transport";case"import_export":return"flow_"+w;default:return null}}async function oe(){l(19,U=!0);let d=fe();d!==null&&await dt(i.solution_name,d,i.scenario_name,i.detail.system.reference_year,i.detail.system.interval_between_years).then(K=>{a=K.data,_=K.unit,l(19,U=!1)})}function x(){if(l(7,n=null),l(10,E=""),i==null){l(0,r=[]);return}switch(m){case"import_export":w=="import"?l(0,r=i.detail.carriers_import):l(0,r=i.detail.carriers_export);break;case"conversion":let d=i.detail.carriers_output;w=="input"&&(d=i.detail.carriers_input),l(0,r=[]);for(const K in d)l(0,r=[...new Set([...r,...d[K]])]);break;default:l(0,r=i.detail.system.set_carriers)}r.length==1&&l(10,E=r[0]),ue()}function ne(){if(l(7,n=[]),m!=null&&E!=null){switch(l(11,b=(i==null?void 0:i.detail.system.set_technologies)??[]),m){case"conversion":l(11,b=[]);let d=i.detail.carriers_input;w=="output"&&(d=i.detail.carriers_output);for(const K in d)d[K].includes(E)&&b.push(K);break;case"storage":l(11,b=(i==null?void 0:i.detail.system.set_storage_technologies.filter(K=>(i==null?void 0:i.detail.reference_carrier[K])==E))??[]);break;case"transport":l(11,b=(i==null?void 0:i.detail.system.set_transport_technologies.filter(K=>(i==null?void 0:i.detail.reference_carrier[K])==E))??[]);break;case"import_export":l(11,b=[]);break}if(_&&b.length>0){let d=_.data.filter(K=>b.includes(K["set_"+m+"_technologies"]));d.length>0&&(g=d[0][0])}b.length==1&&l(12,h=[b[0]]),ue()}}function ge(){l(3,s=u),m=="transport"&&l(3,s=o)}function le(){l(7,n=[]),m!=null&&(v[m]!=null&&l(14,w=v[m][0]),m=="import_export"&&l(20,z="technology"),oe().then(()=>{x(),ne(),ge(),T()}))}function T(){if(m=="import_export"&&l(20,z="node"),z=="technology"?l(13,L=u):l(12,h=b),L.length==0||j.length==0||h.length==0&&m!="import_export"||!a){l(7,n=[]);return}let d={},K={},Ee="node";m=="transport"&&(Ee="edge"),m=="import_export"?(d[Ee]=L,K.carrier=[E]):z=="technology"?(d[Ee]=L,K.technology=h):(d.technology=h,K[Ee]=L);let rt=c.filter(at=>!j.includes(at));l(7,n=pt(a.data,d,K,rt,O=="normalized")),l(21,$.data={datasets:n},$),l(21,$.options.scales.y.title.text=m+" ["+g+"]",$)}function p(d){r=d,l(0,r)}function N(d){u=d,l(1,u)}function J(d){c=d,l(4,c)}function Q(d){i=d,l(8,i)}function f(d){o=d,l(2,o)}function S(d){X=d,l(18,X)}function ee(){m=He(this),l(9,m),l(5,v)}const se=()=>{le()};function ie(d){t.$$.not_equal(v[m],d)&&(v[m]=d,l(5,v))}function de(d){w=d,l(14,w)}const be=d=>{oe(),x(),ne(),T()};function ve(){E=He(this),l(10,E),l(0,r)}const ke=()=>{ne(),T()};function Ce(d){C=d,l(6,C)}function Je(d){z=d,l(20,z)}const Ke=d=>{T()};function Qe(d){W=d,l(16,W)}function Ue(d){O=d,l(17,O)}const We=d=>{T()};function Xe(d){h=d,l(12,h)}function Ze(d){b=d,l(11,b)}const $e=()=>{T()};function xe(d){L=d,l(13,L)}function et(d){s=d,l(3,s)}const tt=d=>{T()};function lt(d){j=d,l(15,j)}function nt(d){c=d,l(4,c)}const ot=d=>{T()};function st(d){$=d,l(21,$)}function it(d){t.$$.not_equal(i.detail.system.reference_year,d)&&(i.detail.system.reference_year=d,l(8,i))}return[r,u,o,s,c,v,C,n,i,m,E,b,h,L,w,j,W,O,X,U,z,$,oe,x,ne,le,T,p,N,J,Q,f,S,ee,se,ie,de,be,ve,ke,Ce,Je,Ke,Qe,Ue,We,Xe,Ze,$e,xe,et,tt,lt,nt,ot,st,it]}class St extends ct{constructor(e){super(),ft(this,e,Dt,yt,_t,{},null,[-1,-1,-1])}}export{St as component};