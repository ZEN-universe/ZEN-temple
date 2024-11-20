import{s as ut,r as A,e as D,a as B,c as I,m as te,g as R,b as M,f as v,o as y,v as me,i as G,h as w,w as Y,y as Re,z as De,A as Ie,B as Ye,C as Fe,t as Ge,d as Je,D as Ve,j as Ke,E as Se,n as Z}from"../chunks/scheduler.BVk0_e6s.js";import{S as dt,i as pt,b as F,c as ae,d as ce,m as _e,t as j,a as P,e as he,f as fe,g as ge}from"../chunks/index.B3JOrRZV.js";import{e as Te}from"../chunks/each.D6YF6ztN.js";import{S as ht,g as gt,f as mt,B as bt}from"../chunks/utils.RN7rXh_g.js";import{R as ye,A as Le}from"../chunks/Radio.DlU7Yl5D.js";function Me(t,e,l){const a=t.slice();return a[65]=e[l],a}function Oe(t,e,l){const a=t.slice();return a[68]=e[l][0],a[69]=e[l][1],a}function ze(t){let e,l,a='<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">Variable Selection</button>',r,d,o,s,_,m,C,n,c,i,f=Te(Object.entries(t[5])),k=[];for(let g=0;g<f.length;g+=1)k[g]=je(Oe(t,f,g));let b=t[5]&&t[9]&&t[5][t[9]]!=null&&qe(t),E=t[9]!=null&&Ne(t);return{c(){e=D("div"),l=D("h2"),l.innerHTML=a,r=B(),d=D("div"),o=D("div"),s=D("select");for(let g=0;g<k.length;g+=1)k[g].c();m=B(),b&&b.c(),C=B(),E&&E.c(),this.h()},l(g){e=I(g,"DIV",{class:!0});var T=M(e);l=I(T,"H2",{class:!0,"data-svelte-h":!0}),te(l)!=="svelte-1b944yg"&&(l.innerHTML=a),r=R(T),d=I(T,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var V=M(d);o=I(V,"DIV",{class:!0});var N=M(o);s=I(N,"SELECT",{});var W=M(s);for(let z=0;z<k.length;z+=1)k[z].l(W);W.forEach(v),m=R(N),b&&b.l(N),C=R(N),E&&E.l(N),N.forEach(v),V.forEach(v),T.forEach(v),this.h()},h(){y(l,"class","accordion-header"),s.disabled=_=t[18]||t[19],t[9]===void 0&&Re(()=>t[34].call(s)),y(o,"class","accordion-body"),y(d,"id","collapseTwo"),y(d,"class","accordion-collapse collapse"),y(d,"data-bs-parent","#accordionExample"),y(e,"class","accordion-item")},m(g,T){G(g,e,T),w(e,l),w(e,r),w(e,d),w(d,o),w(o,s);for(let V=0;V<k.length;V+=1)k[V]&&k[V].m(s,null);De(s,t[9],!0),w(o,m),b&&b.m(o,null),w(o,C),E&&E.m(o,null),n=!0,c||(i=[Ie(s,"change",t[34]),Ie(s,"change",t[35])],c=!0)},p(g,T){if(T[0]&32){f=Te(Object.entries(g[5]));let V;for(V=0;V<f.length;V+=1){const N=Oe(g,f,V);k[V]?k[V].p(N,T):(k[V]=je(N),k[V].c(),k[V].m(s,null))}for(;V<k.length;V+=1)k[V].d(1);k.length=f.length}(!n||T[0]&786432&&_!==(_=g[18]||g[19]))&&(s.disabled=_),T[0]&544&&De(s,g[9]),g[5]&&g[9]&&g[5][g[9]]!=null?b?(b.p(g,T),T[0]&544&&j(b,1)):(b=qe(g),b.c(),j(b,1),b.m(o,C)):b&&(ge(),P(b,1,1,()=>{b=null}),he()),g[9]!=null?E?E.p(g,T):(E=Ne(g),E.c(),E.m(o,null)):E&&(E.d(1),E=null)},i(g){n||(j(b),n=!0)},o(g){P(b),n=!1},d(g){g&&v(e),Ye(k,g),b&&b.d(),E&&E.d(),c=!1,Fe(i)}}}function je(t){let e,l=t[68]+"",a,r,d;return{c(){e=D("option"),a=Ge(l),r=B(),this.h()},l(o){e=I(o,"OPTION",{});var s=M(e);a=Je(s,l),r=R(s),s.forEach(v),this.h()},h(){e.__value=d=t[68],Ve(e,e.__value)},m(o,s){G(o,e,s),w(e,a),w(e,r)},p(o,s){s[0]&32&&l!==(l=o[68]+"")&&Ke(a,l),s[0]&32&&d!==(d=o[68])&&(e.__value=d,Ve(e,e.__value))},d(o){o&&v(e)}}}function qe(t){let e,l,a,r;function d(_){t[36](_)}function o(_){t[37](_)}let s={enabled:!t[18]&&!t[19]};return t[5][t[9]]!==void 0&&(s.options=t[5][t[9]]),t[14]!==void 0&&(s.selected_option=t[14]),e=new ye({props:s}),A.push(()=>F(e,"options",d)),A.push(()=>F(e,"selected_option",o)),e.$on("selection-changed",t[38]),{c(){ae(e.$$.fragment)},l(_){ce(e.$$.fragment,_)},m(_,m){_e(e,_,m),r=!0},p(_,m){const C={};m[0]&786432&&(C.enabled=!_[18]&&!_[19]),!l&&m[0]&544&&(l=!0,C.options=_[5][_[9]],Y(()=>l=!1)),!a&&m[0]&16384&&(a=!0,C.selected_option=_[14],Y(()=>a=!1)),e.$set(C)},i(_){r||(j(e.$$.fragment,_),r=!0)},o(_){P(e.$$.fragment,_),r=!1},d(_){fe(e,_)}}}function Ne(t){let e,l,a,r="Carrier",d,o,s,_,m,C=Te(t[0]),n=[];for(let c=0;c<C.length;c+=1)n[c]=Pe(Me(t,C,c));return{c(){e=D("div"),l=D("div"),a=D("h3"),a.textContent=r,d=B(),o=D("select");for(let c=0;c<n.length;c+=1)n[c].c();this.h()},l(c){e=I(c,"DIV",{class:!0});var i=M(e);l=I(i,"DIV",{class:!0});var f=M(l);a=I(f,"H3",{"data-svelte-h":!0}),te(a)!=="svelte-xc22hm"&&(a.textContent=r),d=R(f),o=I(f,"SELECT",{});var k=M(o);for(let b=0;b<n.length;b+=1)n[b].l(k);k.forEach(v),f.forEach(v),i.forEach(v),this.h()},h(){o.disabled=s=t[18]||t[19],t[10]===void 0&&Re(()=>t[39].call(o)),y(l,"class","col"),y(e,"class","row")},m(c,i){G(c,e,i),w(e,l),w(l,a),w(l,d),w(l,o);for(let f=0;f<n.length;f+=1)n[f]&&n[f].m(o,null);De(o,t[10],!0),_||(m=[Ie(o,"change",t[39]),Ie(o,"change",t[40])],_=!0)},p(c,i){if(i[0]&1){C=Te(c[0]);let f;for(f=0;f<C.length;f+=1){const k=Me(c,C,f);n[f]?n[f].p(k,i):(n[f]=Pe(k),n[f].c(),n[f].m(o,null))}for(;f<n.length;f+=1)n[f].d(1);n.length=C.length}i[0]&786432&&s!==(s=c[18]||c[19])&&(o.disabled=s),i[0]&1025&&De(o,c[10])},d(c){c&&v(e),Ye(n,c),_=!1,Fe(m)}}}function Pe(t){let e,l=t[65]+"",a,r,d;return{c(){e=D("option"),a=Ge(l),r=B(),this.h()},l(o){e=I(o,"OPTION",{});var s=M(e);a=Je(s,l),r=R(s),s.forEach(v),this.h()},h(){e.__value=d=t[65],Ve(e,e.__value)},m(o,s){G(o,e,s),w(e,a),w(e,r)},p(o,s){s[0]&1&&l!==(l=o[65]+"")&&Ke(a,l),s[0]&1&&d!==(d=o[65])&&(e.__value=d,Ve(e,e.__value))},d(o){o&&v(e)}}}function Ae(t){let e,l,a='<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">Data Selection</button>',r,d,o,s,_,m,C,n="Normalisation",c,i,f,k,b,E,g,T,V,N="Year",W,z,X,K,O,H=t[9]!="import_export"&&Be(t);function $(p){t[44](p)}function de(p){t[45](p)}let ne={enabled:!t[18]&&!t[19]};t[16]!==void 0&&(ne.options=t[16]),t[17]!==void 0&&(ne.selected_option=t[17]),i=new ye({props:ne}),A.push(()=>F(i,"options",$)),A.push(()=>F(i,"selected_option",de)),i.$on("selection-changed",t[46]);const ue=[kt,vt],x=[];function oe(p,q){return p[21]=="technology"?0:1}E=oe(t),g=x[E]=ue[E](t);function se(p){t[53](p)}function le(p){t[54](p)}let S={enabled:!t[18]&&!t[19]};return t[15]!==void 0&&(S.selected_elements=t[15]),t[4]!==void 0&&(S.elements=t[4]),z=new Le({props:S}),A.push(()=>F(z,"selected_elements",se)),A.push(()=>F(z,"elements",le)),z.$on("selection-changed",t[55]),{c(){e=D("div"),l=D("h2"),l.innerHTML=a,r=B(),d=D("div"),o=D("div"),s=D("div"),H&&H.c(),_=B(),m=D("div"),C=D("h3"),C.textContent=n,c=B(),ae(i.$$.fragment),b=B(),g.c(),T=B(),V=D("h3"),V.textContent=N,W=B(),ae(z.$$.fragment),this.h()},l(p){e=I(p,"DIV",{class:!0});var q=M(e);l=I(q,"H2",{class:!0,"data-svelte-h":!0}),te(l)!=="svelte-hz94lo"&&(l.innerHTML=a),r=R(q),d=I(q,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var J=M(d);o=I(J,"DIV",{class:!0});var Q=M(o);s=I(Q,"DIV",{class:!0});var u=M(s);H&&H.l(u),_=R(u),m=I(u,"DIV",{class:!0});var L=M(m);C=I(L,"H3",{"data-svelte-h":!0}),te(C)!=="svelte-1273uzu"&&(C.textContent=n),c=R(L),ce(i.$$.fragment,L),L.forEach(v),u.forEach(v),b=R(Q),g.l(Q),T=R(Q),V=I(Q,"H3",{"data-svelte-h":!0}),te(V)!=="svelte-r9e7qt"&&(V.textContent=N),W=R(Q),ce(z.$$.fragment,Q),Q.forEach(v),J.forEach(v),q.forEach(v),this.h()},h(){y(l,"class","accordion-header"),y(m,"class","col-6"),y(s,"class","row"),y(o,"class","accordion-body"),y(d,"id","collapseThree"),y(d,"class","accordion-collapse collapse"),y(d,"data-bs-parent","#accordionExample"),y(e,"class","accordion-item")},m(p,q){G(p,e,q),w(e,l),w(e,r),w(e,d),w(d,o),w(o,s),H&&H.m(s,null),w(s,_),w(s,m),w(m,C),w(m,c),_e(i,m,null),w(o,b),x[E].m(o,null),w(o,T),w(o,V),w(o,W),_e(z,o,null),O=!0},p(p,q){p[9]!="import_export"?H?(H.p(p,q),q[0]&512&&j(H,1)):(H=Be(p),H.c(),j(H,1),H.m(s,_)):H&&(ge(),P(H,1,1,()=>{H=null}),he());const J={};q[0]&786432&&(J.enabled=!p[18]&&!p[19]),!f&&q[0]&65536&&(f=!0,J.options=p[16],Y(()=>f=!1)),!k&&q[0]&131072&&(k=!0,J.selected_option=p[17],Y(()=>k=!1)),i.$set(J);let Q=E;E=oe(p),E===Q?x[E].p(p,q):(ge(),P(x[Q],1,1,()=>{x[Q]=null}),he(),g=x[E],g?g.p(p,q):(g=x[E]=ue[E](p),g.c()),j(g,1),g.m(o,T));const u={};q[0]&786432&&(u.enabled=!p[18]&&!p[19]),!X&&q[0]&32768&&(X=!0,u.selected_elements=p[15],Y(()=>X=!1)),!K&&q[0]&16&&(K=!0,u.elements=p[4],Y(()=>K=!1)),z.$set(u)},i(p){O||(j(H),j(i.$$.fragment,p),j(g),j(z.$$.fragment,p),O=!0)},o(p){P(H),P(i.$$.fragment,p),P(g),P(z.$$.fragment,p),O=!1},d(p){p&&v(e),H&&H.d(),fe(i),x[E].d(),fe(z)}}}function Be(t){let e,l,a="Aggregation",r,d,o,s,_;function m(c){t[41](c)}function C(c){t[42](c)}let n={enabled:!t[18]&&!t[19]};return t[6]!==void 0&&(n.options=t[6]),t[21]!==void 0&&(n.selected_option=t[21]),d=new ye({props:n}),A.push(()=>F(d,"options",m)),A.push(()=>F(d,"selected_option",C)),d.$on("selection-changed",t[43]),{c(){e=D("div"),l=D("h3"),l.textContent=a,r=B(),ae(d.$$.fragment),this.h()},l(c){e=I(c,"DIV",{class:!0});var i=M(e);l=I(i,"H3",{"data-svelte-h":!0}),te(l)!=="svelte-126hufg"&&(l.textContent=a),r=R(i),ce(d.$$.fragment,i),i.forEach(v),this.h()},h(){y(e,"class","col-6")},m(c,i){G(c,e,i),w(e,l),w(e,r),_e(d,e,null),_=!0},p(c,i){const f={};i[0]&786432&&(f.enabled=!c[18]&&!c[19]),!o&&i[0]&64&&(o=!0,f.options=c[6],Y(()=>o=!1)),!s&&i[0]&2097152&&(s=!0,f.selected_option=c[21],Y(()=>s=!1)),d.$set(f)},i(c){_||(j(d.$$.fragment,c),_=!0)},o(c){P(d.$$.fragment,c),_=!1},d(c){c&&v(e),fe(d)}}}function vt(t){let e,l="Node",a,r,d,o,s;function _(n){t[50](n)}function m(n){t[51](n)}let C={enabled:!t[18]&&!t[19]};return t[13]!==void 0&&(C.selected_elements=t[13]),t[3]!==void 0&&(C.elements=t[3]),r=new Le({props:C}),A.push(()=>F(r,"selected_elements",_)),A.push(()=>F(r,"elements",m)),r.$on("selection-changed",t[52]),{c(){e=D("h3"),e.textContent=l,a=B(),ae(r.$$.fragment)},l(n){e=I(n,"H3",{"data-svelte-h":!0}),te(e)!=="svelte-ocjo5w"&&(e.textContent=l),a=R(n),ce(r.$$.fragment,n)},m(n,c){G(n,e,c),G(n,a,c),_e(r,n,c),s=!0},p(n,c){const i={};c[0]&786432&&(i.enabled=!n[18]&&!n[19]),!d&&c[0]&8192&&(d=!0,i.selected_elements=n[13],Y(()=>d=!1)),!o&&c[0]&8&&(o=!0,i.elements=n[3],Y(()=>o=!1)),r.$set(i)},i(n){s||(j(r.$$.fragment,n),s=!0)},o(n){P(r.$$.fragment,n),s=!1},d(n){n&&(v(e),v(a)),fe(r,n)}}}function kt(t){let e,l="Technology",a,r,d,o,s;function _(n){t[47](n)}function m(n){t[48](n)}let C={enabled:!t[18]&&!t[19]};return t[12]!==void 0&&(C.selected_elements=t[12]),t[11]!==void 0&&(C.elements=t[11]),r=new Le({props:C}),A.push(()=>F(r,"selected_elements",_)),A.push(()=>F(r,"elements",m)),r.$on("selection-changed",t[49]),{c(){e=D("h3"),e.textContent=l,a=B(),ae(r.$$.fragment)},l(n){e=I(n,"H3",{"data-svelte-h":!0}),te(e)!=="svelte-q7cxxi"&&(e.textContent=l),a=R(n),ce(r.$$.fragment,n)},m(n,c){G(n,e,c),G(n,a,c),_e(r,n,c),s=!0},p(n,c){const i={};c[0]&786432&&(i.enabled=!n[18]&&!n[19]),!d&&c[0]&4096&&(d=!0,i.selected_elements=n[12],Y(()=>d=!1)),!o&&c[0]&2048&&(o=!0,i.elements=n[11],Y(()=>o=!1)),r.$set(i)},i(n){s||(j(r.$$.fragment,n),s=!0)},o(n){P(r.$$.fragment,n),s=!1},d(n){n&&(v(e),v(a)),fe(r,n)}}}function Ct(t){let e,l,a,r;function d(_){t[56](_)}function o(_){t[57](_)}let s={};return t[22]!==void 0&&(s.config=t[22]),t[20]!==void 0&&(s.plot_name=t[20]),e=new bt({props:s}),A.push(()=>F(e,"config",d)),A.push(()=>F(e,"plot_name",o)),{c(){ae(e.$$.fragment)},l(_){ce(e.$$.fragment,_)},m(_,m){_e(e,_,m),r=!0},p(_,m){const C={};!l&&m[0]&4194304&&(l=!0,C.config=_[22],Y(()=>l=!1)),!a&&m[0]&1048576&&(a=!0,C.plot_name=_[20],Y(()=>a=!1)),e.$set(C)},i(_){r||(j(e.$$.fragment,_),r=!0)},o(_){P(e.$$.fragment,_),r=!1},d(_){fe(e,_)}}}function Et(t){let e,l="No data with this selection.";return{c(){e=D("div"),e.textContent=l,this.h()},l(a){e=I(a,"DIV",{class:!0,"data-svelte-h":!0}),te(e)!=="svelte-1doxial"&&(e.textContent=l),this.h()},h(){y(e,"class","text-center")},m(a,r){G(a,e,r)},p:Z,i:Z,o:Z,d(a){a&&v(e)}}}function wt(t){let e,l="No technologies with this selection.";return{c(){e=D("div"),e.textContent=l,this.h()},l(a){e=I(a,"DIV",{class:!0,"data-svelte-h":!0}),te(e)!=="svelte-1ontq7"&&(e.textContent=l),this.h()},h(){y(e,"class","text-center")},m(a,r){G(a,e,r)},p:Z,i:Z,o:Z,d(a){a&&v(e)}}}function Dt(t){let e;return{c(){e=D("div")},l(l){e=I(l,"DIV",{}),M(e).forEach(v)},m(l,a){G(l,e,a)},p:Z,i:Z,o:Z,d(l){l&&v(e)}}}function It(t){let e;return{c(){e=D("div")},l(l){e=I(l,"DIV",{}),M(e).forEach(v)},m(l,a){G(l,e,a)},p:Z,i:Z,o:Z,d(l){l&&v(e)}}}function Vt(t){let e,l='<div class="spinner-border center" role="status"><span class="visually-hidden">Loading...</span></div>';return{c(){e=D("div"),e.innerHTML=l,this.h()},l(a){e=I(a,"DIV",{class:!0,"data-svelte-h":!0}),te(e)!=="svelte-1a5ljpq"&&(e.innerHTML=l),this.h()},h(){y(e,"class","text-center")},m(a,r){G(a,e,r)},p:Z,i:Z,o:Z,d(a){a&&v(e)}}}function Tt(t){let e,l='<div class="col"><h2>Production</h2></div>',a,r,d,o,s,_,m,C='<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">Solution Selection</button>',n,c,i,f,k,b,E,g,T,V,N,W,z,X,K,O,H,$;function de(u){t[28](u)}function ne(u){t[29](u)}function ue(u){t[30](u)}function x(u){t[31](u)}function oe(u){t[32](u)}function se(u){t[33](u)}let le={enabled:!t[18]&&!t[19]};t[0]!==void 0&&(le.carriers=t[0]),t[1]!==void 0&&(le.nodes=t[1]),t[4]!==void 0&&(le.years=t[4]),t[8]!==void 0&&(le.selected_solution=t[8]),t[2]!==void 0&&(le.edges=t[2]),t[18]!==void 0&&(le.loading=t[18]),f=new ht({props:le}),A.push(()=>F(f,"carriers",de)),A.push(()=>F(f,"nodes",ne)),A.push(()=>F(f,"years",ue)),A.push(()=>F(f,"selected_solution",x)),A.push(()=>F(f,"edges",oe)),A.push(()=>F(f,"loading",se)),f.$on("solution_selected",t[24]);let S=!t[18]&&t[8]&&ze(t),p=!t[19]&&t[10]&&(t[11].length>0||t[9]=="import_export")&&Ae(t);const q=[Vt,It,Dt,wt,Et,Ct],J=[];function Q(u,L){return u[18]||u[19]?0:u[8]==null?1:u[7]==null?2:u[11].length==0&&u[9]!="import_export"?3:u[7].length==0?4:5}return O=Q(t),H=J[O]=q[O](t),{c(){e=D("div"),e.innerHTML=l,a=B(),r=D("div"),d=D("div"),o=D("div"),s=D("div"),_=D("div"),m=D("h2"),m.innerHTML=C,n=B(),c=D("div"),i=D("div"),ae(f.$$.fragment),N=B(),S&&S.c(),W=B(),p&&p.c(),z=B(),X=D("div"),K=D("div"),H.c(),this.h()},l(u){e=I(u,"DIV",{class:!0,"data-svelte-h":!0}),te(e)!=="svelte-1ow2g6f"&&(e.innerHTML=l),a=R(u),r=I(u,"DIV",{class:!0});var L=M(r);d=I(L,"DIV",{class:!0,style:!0});var ee=M(d);o=I(ee,"DIV",{class:!0,style:!0});var ie=M(o);s=I(ie,"DIV",{class:!0,id:!0});var re=M(s);_=I(re,"DIV",{class:!0});var pe=M(_);m=I(pe,"H2",{class:!0,"data-svelte-h":!0}),te(m)!=="svelte-64kjki"&&(m.innerHTML=C),n=R(pe),c=I(pe,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var be=M(c);i=I(be,"DIV",{class:!0});var ve=M(i);ce(f.$$.fragment,ve),ve.forEach(v),be.forEach(v),pe.forEach(v),N=R(re),S&&S.l(re),W=R(re),p&&p.l(re),re.forEach(v),ie.forEach(v),ee.forEach(v),L.forEach(v),z=R(u),X=I(u,"DIV",{class:!0});var ke=M(X);K=I(ke,"DIV",{class:!0,style:!0});var Ce=M(K);H.l(Ce),Ce.forEach(v),ke.forEach(v),this.h()},h(){y(e,"class","row"),y(m,"class","accordion-header"),y(i,"class","accordion-body"),y(c,"id","collapseOne"),y(c,"class","accordion-collapse collapse show"),y(c,"data-bs-parent","#accordionExample"),y(_,"class","accordion-item solution-selection"),y(s,"class","accordion"),y(s,"id","accordionExample"),y(o,"class","filters"),me(o,"position","absolute"),me(o,"width","100%"),y(d,"class","col position-relative"),me(d,"z-index","1"),me(d,"position","relative"),y(r,"class","row"),y(K,"class","col"),me(K,"margin-top","400px"),y(X,"class","row")},m(u,L){G(u,e,L),G(u,a,L),G(u,r,L),w(r,d),w(d,o),w(o,s),w(s,_),w(_,m),w(_,n),w(_,c),w(c,i),_e(f,i,null),w(s,N),S&&S.m(s,null),w(s,W),p&&p.m(s,null),G(u,z,L),G(u,X,L),w(X,K),J[O].m(K,null),$=!0},p(u,L){const ee={};L[0]&786432&&(ee.enabled=!u[18]&&!u[19]),!k&&L[0]&1&&(k=!0,ee.carriers=u[0],Y(()=>k=!1)),!b&&L[0]&2&&(b=!0,ee.nodes=u[1],Y(()=>b=!1)),!E&&L[0]&16&&(E=!0,ee.years=u[4],Y(()=>E=!1)),!g&&L[0]&256&&(g=!0,ee.selected_solution=u[8],Y(()=>g=!1)),!T&&L[0]&4&&(T=!0,ee.edges=u[2],Y(()=>T=!1)),!V&&L[0]&262144&&(V=!0,ee.loading=u[18],Y(()=>V=!1)),f.$set(ee),!u[18]&&u[8]?S?(S.p(u,L),L[0]&262400&&j(S,1)):(S=ze(u),S.c(),j(S,1),S.m(s,W)):S&&(ge(),P(S,1,1,()=>{S=null}),he()),!u[19]&&u[10]&&(u[11].length>0||u[9]=="import_export")?p?(p.p(u,L),L[0]&527872&&j(p,1)):(p=Ae(u),p.c(),j(p,1),p.m(s,null)):p&&(ge(),P(p,1,1,()=>{p=null}),he());let ie=O;O=Q(u),O===ie?J[O].p(u,L):(ge(),P(J[ie],1,1,()=>{J[ie]=null}),he(),H=J[O],H?H.p(u,L):(H=J[O]=q[O](u),H.c()),j(H,1),H.m(K,null))},i(u){$||(j(f.$$.fragment,u),j(S),j(p),j(H),$=!0)},o(u){P(f.$$.fragment,u),P(S),P(p),P(H),$=!1},d(u){u&&(v(e),v(a),v(r),v(z),v(X)),fe(f),S&&S.d(),p&&p.d(),J[O].d()}}}function Ht(t,e,l){let a,r=[],d=[],o=[],s=[],_=[],m={conversion:["input","output"],storage:["charge","discharge"],transport:null,import_export:["import","export"]},C=["technology","node"],n=null,c=null,i=null,f=null,k=null,b=[],E=[],g=[],T=null,V=[],N=["not_normalized","normalized"],W="not_normalized",z=!1,X=!1,K="plot",O="node",$={type:"bar",data:{datasets:[]},options:{responsive:!0,scales:{x:{stacked:!0,title:{display:!0,text:"Year"}},y:{stacked:!0,title:{display:!0,text:f+" ["+ue()+"]"}}}}};function de(){l(15,V=_),l(13,g=d),l(12,E=b)}function ne(){switch(f){case"conversion":return"flow_conversion_"+T;case"storage":return"flow_storage_"+T;case"transport":return"flow_transport";case"import_export":return"flow_"+T;default:return null}}function ue(){if(c===null)return"";for(const h of c.data)if(b[0]==h.technology&&(h.carrier==k||h.carrier===void 0))return h[0];return""}async function x(){l(19,X=!0);let h=ne();h!==null&&await gt(i.solution_name,h,i.scenario_name,i.detail.system.reference_year,i.detail.system.interval_between_years).then(U=>{U.data!==null&&(a=U.data,c=U.unit,l(19,X=!1))})}function oe(){if(l(7,n=null),l(10,k=""),i==null){l(0,r=[]);return}switch(f){case"import_export":T=="import"?l(0,r=i.detail.carriers_import):l(0,r=i.detail.carriers_export);break;case"conversion":let h=i.detail.carriers_output;T=="input"&&(h=i.detail.carriers_input),l(0,r=[]);for(const U in h)l(0,r=[...new Set([...r,...h[U]])]);break;default:l(0,r=i.detail.system.set_carriers)}r.length==1&&l(10,k=r[0]),de()}function se(){if(l(7,n=[]),f!=null&&k!=null){switch(l(11,b=(i==null?void 0:i.detail.system.set_technologies)??[]),f){case"conversion":l(11,b=[]);let h=i.detail.carriers_input;T=="output"&&(h=i.detail.carriers_output);for(const U in h)h[U].includes(k)&&b.push(U);break;case"storage":l(11,b=(i==null?void 0:i.detail.system.set_storage_technologies.filter(U=>(i==null?void 0:i.detail.reference_carrier[U])==k))??[]);break;case"transport":l(11,b=(i==null?void 0:i.detail.system.set_transport_technologies.filter(U=>(i==null?void 0:i.detail.reference_carrier[U])==k))??[]);break;case"import_export":l(11,b=[]);break}b.length==1&&l(12,E=[b[0]]),de()}}function le(){l(3,s=d),f=="transport"&&l(3,s=o)}function S(){l(7,n=[]),f!=null&&(m[f]!=null&&l(14,T=m[f][0]),f=="import_export"&&l(21,O="technology"),x().then(()=>{oe(),se(),le(),p()}))}function p(){if(f=="import_export"&&l(21,O="node"),O=="technology"?l(13,g=d):l(12,E=b),g.length==0||V.length==0||E.length==0&&f!="import_export"||!a){l(7,n=[]);return}let h={},U={},Ee="node";f=="transport"&&(Ee="edge"),f=="import_export"?(h[Ee]=g,U.carrier=[k]):O=="technology"?(h[Ee]=g,U.technology=E):(h.technology=E,U[Ee]=g);let _t=_.filter(He=>!V.includes(He)),ft=a.data.filter(He=>He.carrier==k);l(7,n=mt(ft,h,U,_t,W=="normalized")),l(22,$.data={datasets:n},$),l(22,$.options.scales.y.title.text=f+" ["+ue()+"]",$);let we=i.solution_name.split(".");l(20,K=[we[(we==null?void 0:we.length)-1],i==null?void 0:i.scenario_name,ne(),k].join("_"))}function q(h){r=h,l(0,r)}function J(h){d=h,l(1,d)}function Q(h){_=h,l(4,_)}function u(h){i=h,l(8,i)}function L(h){o=h,l(2,o)}function ee(h){z=h,l(18,z)}function ie(){f=Se(this),l(9,f),l(5,m)}const re=()=>{S()};function pe(h){t.$$.not_equal(m[f],h)&&(m[f]=h,l(5,m))}function be(h){T=h,l(14,T)}const ve=h=>{x(),oe(),se(),p()};function ke(){k=Se(this),l(10,k),l(0,r)}const Ce=()=>{se(),p()};function Qe(h){C=h,l(6,C)}function Ue(h){O=h,l(21,O)}const We=h=>{p()};function Xe(h){N=h,l(16,N)}function Ze(h){W=h,l(17,W)}const $e=h=>{p()};function xe(h){E=h,l(12,E)}function et(h){b=h,l(11,b)}const tt=()=>{p()};function lt(h){g=h,l(13,g)}function nt(h){s=h,l(3,s)}const ot=h=>{p()};function st(h){V=h,l(15,V)}function it(h){_=h,l(4,_)}const rt=h=>{p()};function at(h){$=h,l(22,$)}function ct(h){K=h,l(20,K)}return[r,d,o,s,_,m,C,n,i,f,k,b,E,g,T,V,N,W,z,X,K,O,$,x,oe,se,S,p,q,J,Q,u,L,ee,ie,re,pe,be,ve,ke,Ce,Qe,Ue,We,Xe,Ze,$e,xe,et,tt,lt,nt,ot,st,it,rt,at,ct]}class zt extends dt{constructor(e){super(),pt(this,e,Ht,Tt,ut,{},null,[-1,-1,-1])}}export{zt as component};