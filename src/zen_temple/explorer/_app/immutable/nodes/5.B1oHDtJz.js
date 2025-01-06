import{s as nt,r as Q,e as C,a as z,c as w,m as Y,g as F,b as q,f as g,o as T,v as ke,i as N,h as I,w as U,x as Ae,y as Je,z as Ce,A as we,B as Ke,C as Qe,t as ye,d as Ee,D as De,j as Me,E as Oe,n as B,F as qe}from"../chunks/scheduler.BVk0_e6s.js";import{S as ot,i as st,b as W,c as he,d as pe,m as ge,t as J,a as X,e as Ie,f as me,g as Ve}from"../chunks/index.B3JOrRZV.js";import{e as Te}from"../chunks/each.D6YF6ztN.js";import{S as it,f as at,B as rt,g as ct}from"../chunks/utils.vTcOBzXM.js";import{R as Be,A as Ne}from"../chunks/Radio.CXSHN0HG.js";import{g as _t}from"../chunks/variables.CqS7hfz2.js";function Pe(l,e,t){const n=l.slice();return n[58]=e[t],n}function je(l,e,t){const n=l.slice();return n[61]=e[t],n}function ze(l){let e,t,n='<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">Variable Selection</button>',o,u,s,a,d="Variable",y,h,i,_,r,m,v,S,P,A=Te(l[2]),L=[];for(let c=0;c<A.length;c+=1)L[c]=Fe(je(l,A,c));let E=l[3].length>0&&Re(l),D=l[0]&&l[10]&&l[6].length>0&&l[4].length>0&&Ge(l);return{c(){e=C("div"),t=C("h2"),t.innerHTML=n,o=z(),u=C("div"),s=C("div"),a=C("h3"),a.textContent=d,y=z(),h=C("select");for(let c=0;c<L.length;c+=1)L[c].c();_=z(),E&&E.c(),r=z(),D&&D.c(),m=Ae(),this.h()},l(c){e=w(c,"DIV",{class:!0});var V=q(e);t=w(V,"H2",{class:!0,"data-svelte-h":!0}),Y(t)!=="svelte-18ejqb9"&&(t.innerHTML=n),o=F(V),u=w(V,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var b=q(u);s=w(b,"DIV",{class:!0});var H=q(s);a=w(H,"H3",{"data-svelte-h":!0}),Y(a)!=="svelte-aqa7bk"&&(a.textContent=d),y=F(H),h=w(H,"SELECT",{});var ee=q(h);for(let Z=0;Z<L.length;Z+=1)L[Z].l(ee);ee.forEach(g),_=F(H),E&&E.l(H),H.forEach(g),b.forEach(g),V.forEach(g),r=F(c),D&&D.l(c),m=Ae(),this.h()},h(){T(t,"class","accordion-header"),h.disabled=i=l[16]||l[15],l[9]===void 0&&Je(()=>l[29].call(h)),T(s,"class","accordion-body"),T(u,"id","collapseTwo"),T(u,"class","accordion-collapse collapse"),T(u,"data-bs-parent","#accordionExample"),T(e,"class","accordion-item variable-selection")},m(c,V){N(c,e,V),I(e,t),I(e,o),I(e,u),I(u,s),I(s,a),I(s,y),I(s,h);for(let b=0;b<L.length;b+=1)L[b]&&L[b].m(h,null);Ce(h,l[9],!0),I(s,_),E&&E.m(s,null),N(c,r,V),D&&D.m(c,V),N(c,m,V),v=!0,S||(P=[we(h,"change",l[29]),we(h,"change",l[30])],S=!0)},p(c,V){if(V[0]&4){A=Te(c[2]);let b;for(b=0;b<A.length;b+=1){const H=je(c,A,b);L[b]?L[b].p(H,V):(L[b]=Fe(H),L[b].c(),L[b].m(h,null))}for(;b<L.length;b+=1)L[b].d(1);L.length=A.length}(!v||V[0]&98304&&i!==(i=c[16]||c[15]))&&(h.disabled=i),V[0]&516&&Ce(h,c[9]),c[3].length>0?E?E.p(c,V):(E=Re(c),E.c(),E.m(s,null)):E&&(E.d(1),E=null),c[0]&&c[10]&&c[6].length>0&&c[4].length>0?D?(D.p(c,V),V[0]&1105&&J(D,1)):(D=Ge(c),D.c(),J(D,1),D.m(m.parentNode,m)):D&&(Ve(),X(D,1,1,()=>{D=null}),Ie())},i(c){v||(J(D),v=!0)},o(c){X(D),v=!1},d(c){c&&(g(e),g(r),g(m)),Ke(L,c),E&&E.d(),D&&D.d(c),S=!1,Qe(P)}}}function Fe(l){let e,t=l[61]+"",n,o,u;return{c(){e=C("option"),n=ye(t),o=z(),this.h()},l(s){e=w(s,"OPTION",{});var a=q(e);n=Ee(a,t),o=F(a),a.forEach(g),this.h()},h(){e.__value=u=l[61],De(e,e.__value)},m(s,a){N(s,e,a),I(e,n),I(e,o)},p(s,a){a[0]&4&&t!==(t=s[61]+"")&&Me(n,t),a[0]&4&&u!==(u=s[61])&&(e.__value=u,De(e,e.__value))},d(s){s&&g(e)}}}function Re(l){let e,t="Carrier",n,o,u,s=(l[16]||l[15])+"",a,d,y,h,i=Te(l[3]),_=[];for(let r=0;r<i.length;r+=1)_[r]=Ye(Pe(l,i,r));return{c(){e=C("h3"),e.textContent=t,n=z(),o=C("select");for(let r=0;r<_.length;r+=1)_[r].c();u=ye(`
                                        disabled=`),a=ye(s),this.h()},l(r){e=w(r,"H3",{"data-svelte-h":!0}),Y(e)!=="svelte-xc22hm"&&(e.textContent=t),n=F(r),o=w(r,"SELECT",{});var m=q(o);for(let v=0;v<_.length;v+=1)_[v].l(m);u=Ee(m,`
                                        disabled=`),a=Ee(m,s),m.forEach(g),this.h()},h(){o.disabled=d=l[16]||l[15],l[10]===void 0&&Je(()=>l[31].call(o))},m(r,m){N(r,e,m),N(r,n,m),N(r,o,m);for(let v=0;v<_.length;v+=1)_[v]&&_[v].m(o,null);I(o,u),I(o,a),Ce(o,l[10],!0),y||(h=[we(o,"change",l[31]),we(o,"change",l[32])],y=!0)},p(r,m){if(m[0]&8){i=Te(r[3]);let v;for(v=0;v<i.length;v+=1){const S=Pe(r,i,v);_[v]?_[v].p(S,m):(_[v]=Ye(S),_[v].c(),_[v].m(o,u))}for(;v<_.length;v+=1)_[v].d(1);_.length=i.length}m[0]&98304&&s!==(s=(r[16]||r[15])+"")&&Me(a,s),m[0]&98304&&d!==(d=r[16]||r[15])&&(o.disabled=d),m[0]&1032&&Ce(o,r[10])},d(r){r&&(g(e),g(n),g(o)),Ke(_,r),y=!1,Qe(h)}}}function Ye(l){let e,t=l[58]+"",n,o;return{c(){e=C("option"),n=ye(t),this.h()},l(u){e=w(u,"OPTION",{});var s=q(e);n=Ee(s,t),s.forEach(g),this.h()},h(){e.__value=o=l[58],De(e,e.__value)},m(u,s){N(u,e,s),I(e,n)},p(u,s){s[0]&8&&t!==(t=u[58]+"")&&Me(n,t),s[0]&8&&o!==(o=u[58])&&(e.__value=o,De(e,e.__value))},d(u){u&&g(e)}}}function Ge(l){let e,t,n='<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">Data Selection</button>',o,u,s,a,d,y,h="Aggregation",i,_,r,m,v,S,P,A="Plot Style",L,E,D,c,V,b,H,ee,Z,ne="Year",M,G,K,ie,f;function O(k){l[33](k)}function j(k){l[34](k)}let te={};l[8]!==void 0&&(te.options=l[8]),l[11]!==void 0&&(te.selected_option=l[11]),_=new Be({props:te}),Q.push(()=>W(_,"options",O)),Q.push(()=>W(_,"selected_option",j)),_.$on("selection-changed",l[35]);function ae(k){l[36](k)}function re(k){l[37](k)}let ce={};l[18]!==void 0&&(ce.options=l[18]),l[19]!==void 0&&(ce.selected_option=l[19]),E=new Be({props:ce}),Q.push(()=>W(E,"options",ae)),Q.push(()=>W(E,"selected_option",re)),E.$on("selection-changed",l[38]);const ue=[dt,ut],$=[];function de(k,R){return k[11]=="technology"?0:1}b=de(l),H=$[b]=ue[b](l);function He(k){l[45](k)}function Le(k){l[46](k)}let ve={};return l[13]!==void 0&&(ve.selected_elements=l[13]),l[5]!==void 0&&(ve.elements=l[5]),G=new Ne({props:ve}),Q.push(()=>W(G,"selected_elements",He)),Q.push(()=>W(G,"elements",Le)),G.$on("selection-changed",l[47]),{c(){e=C("div"),t=C("h2"),t.innerHTML=n,o=z(),u=C("div"),s=C("div"),a=C("div"),d=C("div"),y=C("h3"),y.textContent=h,i=z(),he(_.$$.fragment),v=z(),S=C("div"),P=C("h3"),P.textContent=A,L=z(),he(E.$$.fragment),V=z(),H.c(),ee=z(),Z=C("h3"),Z.textContent=ne,M=z(),he(G.$$.fragment),this.h()},l(k){e=w(k,"DIV",{class:!0});var R=q(e);t=w(R,"H2",{class:!0,"data-svelte-h":!0}),Y(t)!=="svelte-1btd1mx"&&(t.innerHTML=n),o=F(R),u=w(R,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var _e=q(u);s=w(_e,"DIV",{class:!0});var x=q(s);a=w(x,"DIV",{class:!0});var oe=q(a);d=w(oe,"DIV",{class:!0});var se=q(d);y=w(se,"H3",{"data-svelte-h":!0}),Y(y)!=="svelte-126hufg"&&(y.textContent=h),i=F(se),pe(_.$$.fragment,se),se.forEach(g),v=F(oe),S=w(oe,"DIV",{class:!0});var be=q(S);P=w(be,"H3",{"data-svelte-h":!0}),Y(P)!=="svelte-7awz6y"&&(P.textContent=A),L=F(be),pe(E.$$.fragment,be),be.forEach(g),oe.forEach(g),V=F(x),H.l(x),ee=F(x),Z=w(x,"H3",{"data-svelte-h":!0}),Y(Z)!=="svelte-r9e7qt"&&(Z.textContent=ne),M=F(x),pe(G.$$.fragment,x),x.forEach(g),_e.forEach(g),R.forEach(g),this.h()},h(){T(t,"class","accordion-header"),T(d,"class","col-6"),T(S,"class","col-6"),T(a,"class","row"),T(s,"class","accordion-body"),T(u,"id","collapseThree"),T(u,"class","accordion-collapse collapse"),T(u,"data-bs-parent","#accordionExample"),T(e,"class","accordion-item")},m(k,R){N(k,e,R),I(e,t),I(e,o),I(e,u),I(u,s),I(s,a),I(a,d),I(d,y),I(d,i),ge(_,d,null),I(a,v),I(a,S),I(S,P),I(S,L),ge(E,S,null),I(s,V),$[b].m(s,null),I(s,ee),I(s,Z),I(s,M),ge(G,s,null),f=!0},p(k,R){const _e={};!r&&R[0]&256&&(r=!0,_e.options=k[8],U(()=>r=!1)),!m&&R[0]&2048&&(m=!0,_e.selected_option=k[11],U(()=>m=!1)),_.$set(_e);const x={};!D&&R[0]&262144&&(D=!0,x.options=k[18],U(()=>D=!1)),!c&&R[0]&524288&&(c=!0,x.selected_option=k[19],U(()=>c=!1)),E.$set(x);let oe=b;b=de(k),b===oe?$[b].p(k,R):(Ve(),X($[oe],1,1,()=>{$[oe]=null}),Ie(),H=$[b],H?H.p(k,R):(H=$[b]=ue[b](k),H.c()),J(H,1),H.m(s,ee));const se={};!K&&R[0]&8192&&(K=!0,se.selected_elements=k[13],U(()=>K=!1)),!ie&&R[0]&32&&(ie=!0,se.elements=k[5],U(()=>ie=!1)),G.$set(se)},i(k){f||(J(_.$$.fragment,k),J(E.$$.fragment,k),J(H),J(G.$$.fragment,k),f=!0)},o(k){X(_.$$.fragment,k),X(E.$$.fragment,k),X(H),X(G.$$.fragment,k),f=!1},d(k){k&&g(e),me(_),me(E),$[b].d(),me(G)}}}function ut(l){let e,t="Node",n,o,u,s,a;function d(i){l[42](i)}function y(i){l[43](i)}let h={};return l[14]!==void 0&&(h.selected_elements=l[14]),l[4]!==void 0&&(h.elements=l[4]),o=new Ne({props:h}),Q.push(()=>W(o,"selected_elements",d)),Q.push(()=>W(o,"elements",y)),o.$on("selection-changed",l[44]),{c(){e=C("h3"),e.textContent=t,n=z(),he(o.$$.fragment)},l(i){e=w(i,"H3",{"data-svelte-h":!0}),Y(e)!=="svelte-ocjo5w"&&(e.textContent=t),n=F(i),pe(o.$$.fragment,i)},m(i,_){N(i,e,_),N(i,n,_),ge(o,i,_),a=!0},p(i,_){const r={};!u&&_[0]&16384&&(u=!0,r.selected_elements=i[14],U(()=>u=!1)),!s&&_[0]&16&&(s=!0,r.elements=i[4],U(()=>s=!1)),o.$set(r)},i(i){a||(J(o.$$.fragment,i),a=!0)},o(i){X(o.$$.fragment,i),a=!1},d(i){i&&(g(e),g(n)),me(o,i)}}}function dt(l){let e,t="Technology",n,o,u,s,a;function d(i){l[39](i)}function y(i){l[40](i)}let h={};return l[12]!==void 0&&(h.selected_elements=l[12]),l[6]!==void 0&&(h.elements=l[6]),o=new Ne({props:h}),Q.push(()=>W(o,"selected_elements",d)),Q.push(()=>W(o,"elements",y)),o.$on("selection-changed",l[41]),{c(){e=C("h3"),e.textContent=t,n=z(),he(o.$$.fragment)},l(i){e=w(i,"H3",{"data-svelte-h":!0}),Y(e)!=="svelte-q7cxxi"&&(e.textContent=t),n=F(i),pe(o.$$.fragment,i)},m(i,_){N(i,e,_),N(i,n,_),ge(o,i,_),a=!0},p(i,_){const r={};!u&&_[0]&4096&&(u=!0,r.selected_elements=i[12],U(()=>u=!1)),!s&&_[0]&64&&(s=!0,r.elements=i[6],U(()=>s=!1)),o.$set(r)},i(i){a||(J(o.$$.fragment,i),a=!0)},o(i){X(o.$$.fragment,i),a=!1},d(i){i&&(g(e),g(n)),me(o,i)}}}function ft(l){let e,t,n,o;function u(d){l[48](d)}function s(d){l[49](d)}let a={};return l[20]!==void 0&&(a.config=l[20]),l[17]!==void 0&&(a.plot_name=l[17]),e=new rt({props:a}),Q.push(()=>W(e,"config",u)),Q.push(()=>W(e,"plot_name",s)),{c(){he(e.$$.fragment)},l(d){pe(e.$$.fragment,d)},m(d,y){ge(e,d,y),o=!0},p(d,y){const h={};!t&&y[0]&1048576&&(t=!0,h.config=d[20],U(()=>t=!1)),!n&&y[0]&131072&&(n=!0,h.plot_name=d[17],U(()=>n=!1)),e.$set(h)},i(d){o||(J(e.$$.fragment,d),o=!0)},o(d){X(e.$$.fragment,d),o=!1},d(d){me(e,d)}}}function ht(l){let e,t="No data with this selection.";return{c(){e=C("div"),e.textContent=t,this.h()},l(n){e=w(n,"DIV",{class:!0,"data-svelte-h":!0}),Y(e)!=="svelte-1doxial"&&(e.textContent=t),this.h()},h(){T(e,"class","text-center")},m(n,o){N(n,e,o)},p:B,i:B,o:B,d(n){n&&g(e)}}}function pt(l){let e,t="No locations with this selection.";return{c(){e=C("div"),e.textContent=t,this.h()},l(n){e=w(n,"DIV",{class:!0,"data-svelte-h":!0}),Y(e)!=="svelte-tr8mx7"&&(e.textContent=t),this.h()},h(){T(e,"class","text-center")},m(n,o){N(n,e,o)},p:B,i:B,o:B,d(n){n&&g(e)}}}function gt(l){let e,t="No data with this selection.";return{c(){e=C("div"),e.textContent=t,this.h()},l(n){e=w(n,"DIV",{class:!0,"data-svelte-h":!0}),Y(e)!=="svelte-1doxial"&&(e.textContent=t),this.h()},h(){T(e,"class","text-center")},m(n,o){N(n,e,o)},p:B,i:B,o:B,d(n){n&&g(e)}}}function mt(l){let e,t="No solution selected.";return{c(){e=C("div"),e.textContent=t,this.h()},l(n){e=w(n,"DIV",{class:!0,"data-svelte-h":!0}),Y(e)!=="svelte-17x0k81"&&(e.textContent=t),this.h()},h(){T(e,"class","text-center")},m(n,o){N(n,e,o)},p:B,i:B,o:B,d(n){n&&g(e)}}}function bt(l){let e,t="No carriers with this selection.";return{c(){e=C("div"),e.textContent=t,this.h()},l(n){e=w(n,"DIV",{class:!0,"data-svelte-h":!0}),Y(e)!=="svelte-1wht3n0"&&(e.textContent=t),this.h()},h(){T(e,"class","text-center")},m(n,o){N(n,e,o)},p:B,i:B,o:B,d(n){n&&g(e)}}}function vt(l){let e,t="No technologies with this selection.";return{c(){e=C("div"),e.textContent=t,this.h()},l(n){e=w(n,"DIV",{class:!0,"data-svelte-h":!0}),Y(e)!=="svelte-1ontq7"&&(e.textContent=t),this.h()},h(){T(e,"class","text-center")},m(n,o){N(n,e,o)},p:B,i:B,o:B,d(n){n&&g(e)}}}function kt(l){let e,t='<div class="spinner-border center" role="status"><span class="visually-hidden">Loading...</span></div>';return{c(){e=C("div"),e.innerHTML=t,this.h()},l(n){e=w(n,"DIV",{class:!0,"data-svelte-h":!0}),Y(e)!=="svelte-57s7b4"&&(e.innerHTML=t),this.h()},h(){T(e,"class","text-center")},m(n,o){N(n,e,o)},p:B,i:B,o:B,d(n){n&&g(e)}}}function Ct(l){let e,t='<div class="col"><h2>Energy Balance Storage</h2></div>',n,o,u,s,a,d,y,h='<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">Solution Selection</button>',i,_,r,m,v,S,P,A,L,E,D,c,V,b;function H(f){l[25](f)}function ee(f){l[26](f)}function Z(f){l[27](f)}let ne={enabled:!l[16]&&!l[15]};l[5]!==void 0&&(ne.years=l[5]),l[7]!==void 0&&(ne.selected_solution=l[7]),l[15]!==void 0&&(ne.loading=l[15]),m=new it({props:ne}),Q.push(()=>W(m,"years",H)),Q.push(()=>W(m,"selected_solution",ee)),Q.push(()=>W(m,"loading",Z)),m.$on("solution_selected",l[28]);let M=!l[15]&&l[7]&&ze(l);const G=[kt,vt,bt,mt,gt,pt,ht,ft],K=[];function ie(f,O){return f[15]||f[16]?0:f[6].length==0?1:f[3].length==0?2:f[7]==null?3:f[1]==null?4:f[4].length==0?5:f[1].length==0?6:7}return c=ie(l),V=K[c]=G[c](l),{c(){e=C("div"),e.innerHTML=t,n=z(),o=C("div"),u=C("div"),s=C("div"),a=C("div"),d=C("div"),y=C("h2"),y.innerHTML=h,i=z(),_=C("div"),r=C("div"),he(m.$$.fragment),A=z(),M&&M.c(),L=z(),E=C("div"),D=C("div"),V.c(),this.h()},l(f){e=w(f,"DIV",{class:!0,"data-svelte-h":!0}),Y(e)!=="svelte-1st2n0t"&&(e.innerHTML=t),n=F(f),o=w(f,"DIV",{class:!0,style:!0});var O=q(o);u=w(O,"DIV",{class:!0});var j=q(u);s=w(j,"DIV",{class:!0,style:!0});var te=q(s);a=w(te,"DIV",{class:!0,id:!0});var ae=q(a);d=w(ae,"DIV",{class:!0});var re=q(d);y=w(re,"H2",{class:!0,"data-svelte-h":!0}),Y(y)!=="svelte-1oln34a"&&(y.innerHTML=h),i=F(re),_=w(re,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var ce=q(_);r=w(ce,"DIV",{class:!0});var ue=q(r);pe(m.$$.fragment,ue),ue.forEach(g),ce.forEach(g),re.forEach(g),A=F(ae),M&&M.l(ae),ae.forEach(g),te.forEach(g),j.forEach(g),O.forEach(g),L=F(f),E=w(f,"DIV",{class:!0,style:!0});var $=q(E);D=w($,"DIV",{class:!0});var de=q(D);V.l(de),de.forEach(g),$.forEach(g),this.h()},h(){T(e,"class","row"),T(y,"class","accordion-header"),T(r,"class","accordion-body"),T(_,"id","collapseOne"),T(_,"class","accordion-collapse collapse show"),T(_,"data-bs-parent","#accordionExample"),T(d,"class","accordion-item solution-selection"),T(a,"class","accordion"),T(a,"id","accordionExample"),T(s,"class","filters"),ke(s,"position","absolute"),ke(s,"width","100%"),T(u,"class","col position-relative"),T(o,"class","row"),ke(o,"z-index","1"),ke(o,"position","relative"),T(D,"class","row"),T(E,"class","col"),ke(E,"margin-top","400px")},m(f,O){N(f,e,O),N(f,n,O),N(f,o,O),I(o,u),I(u,s),I(s,a),I(a,d),I(d,y),I(d,i),I(d,_),I(_,r),ge(m,r,null),I(a,A),M&&M.m(a,null),N(f,L,O),N(f,E,O),I(E,D),K[c].m(D,null),b=!0},p(f,O){const j={};O[0]&98304&&(j.enabled=!f[16]&&!f[15]),!v&&O[0]&32&&(v=!0,j.years=f[5],U(()=>v=!1)),!S&&O[0]&128&&(S=!0,j.selected_solution=f[7],U(()=>S=!1)),!P&&O[0]&32768&&(P=!0,j.loading=f[15],U(()=>P=!1)),m.$set(j),!f[15]&&f[7]?M?(M.p(f,O),O[0]&32896&&J(M,1)):(M=ze(f),M.c(),J(M,1),M.m(a,null)):M&&(Ve(),X(M,1,1,()=>{M=null}),Ie());let te=c;c=ie(f),c===te?K[c].p(f,O):(Ve(),X(K[te],1,1,()=>{K[te]=null}),Ie(),V=K[c],V?V.p(f,O):(V=K[c]=G[c](f),V.c()),J(V,1),V.m(D,null))},i(f){b||(J(m.$$.fragment,f),J(M),J(V),b=!0)},o(f){X(m.$$.fragment,f),X(M),X(V),b=!1},d(f){f&&(g(e),g(n),g(o),g(L),g(E)),me(m),M&&M.d(),K[c].d()}}}function wt(l,e,t){let n=null,o=null,u=[],s=[],a=[],d=[],y=[],h=null,i=["technology","node"],_=null,r=null,m=null,v="technology",S=[],P=[],A=[],L=!1,E=[],D=!1,c="",V=["Line","Bar (stacked)"],b="Line",H={type:"bar",data:{datasets:E},options:{responsive:!0,scales:{x:{stacked:!0,title:{display:!0,text:"Year"}},y:{stacked:!0,title:{display:!0,text:r}}}}};async function ee(){t(14,A=a),t(12,S=y),t(13,P=d),t(11,v="node"),await qe()}async function Z(){if(t(16,D=!0),t(0,n=null),await qe(),r===null){t(16,D=!1);return}let p=await ct(h.solution_name,_t(r),h.scenario_name,h.detail.system.reference_year,h.detail.system.interval_between_years);t(0,n=p.data),_=p.unit,t(16,D=!1)}function ne(){t(2,u=["storage_level","flow_storage_charge","flow_storage_discharge","flow_storage_inflow","flow_storage_spillage"].filter(p=>h.components.includes(p))),t(0,n=null),t(9,r=null),t(1,o=null),t(10,m=null)}async function M(){t(16,D=!0),await Z(),f(),O(),K(),ee(),j(),t(16,D=!1)}function G(){f(),O(),K(),ee(),j()}function K(){t(4,a=Array.from(new Set(n.data.map(p=>p.node)))),t(14,A=a)}function ie(){try{return _.data[0][0]}catch{return""}}function f(){if(t(3,s=[]),!n)return;let p=Array.from(n.data.map(le=>le.technology));n.data.forEach(le=>{let Se=le.technology,fe=h.detail.reference_carrier[Se];!s.includes(fe)&&p.includes(le.technology)&&s.push(fe)}),s.length>0&&t(10,m=s[0])}function O(){let p=Array.from(new Set(n.data.map(le=>le.technology)));t(6,y=p.filter(le=>(h==null?void 0:h.detail.reference_carrier[le])==m)),t(12,S=y)}function j(){if(v=="technology"?t(14,A=a):t(12,S=y),r==null||A.length==0||P.length==0||S.length==0||n===null){t(1,o=null);return}let p={},le={};v=="technology"?(p.node=A,le.technology=S):(p.technology=S,le.node=A);let Se=d.filter(lt=>!P.includes(lt));t(1,o=at(n.data,p,le,Se,!1,b=="Line"?"line":"bar")),t(20,H.data={datasets:o},H),t(20,H.options.scales.y.title.text=r+" ["+ie()+"]",H),t(20,H.options.scales.y.stacked=b!="Line",H);let fe=h.solution_name.split(".");t(17,c=[fe[(fe==null?void 0:fe.length)-1],h==null?void 0:h.scenario_name,r,m].join("_"))}function te(p){d=p,t(5,d)}function ae(p){h=p,t(7,h)}function re(p){L=p,t(15,L)}const ce=()=>{ne()};function ue(){r=Oe(this),t(9,r),t(2,u)}const $=p=>{M()};function de(){m=Oe(this),t(10,m),t(3,s)}const He=()=>{G()};function Le(p){i=p,t(8,i)}function ve(p){v=p,t(11,v)}const k=p=>{j()};function R(p){V=p,t(18,V)}function _e(p){b=p,t(19,b)}const x=p=>{j()};function oe(p){S=p,t(12,S)}function se(p){y=p,t(6,y)}const be=()=>{j()};function Ue(p){A=p,t(14,A)}function We(p){a=p,t(4,a)}const Xe=p=>{j()};function Ze(p){P=p,t(13,P)}function xe(p){d=p,t(5,d)}const $e=p=>{j()};function et(p){H=p,t(20,H)}function tt(p){c=p,t(17,c)}return[n,o,u,s,a,d,y,h,i,r,m,v,S,P,A,L,D,c,V,b,H,ne,M,G,j,te,ae,re,ce,ue,$,de,He,Le,ve,k,R,_e,x,oe,se,be,Ue,We,Xe,Ze,xe,$e,et,tt]}class Ht extends ot{constructor(e){super(),st(this,e,wt,Ct,nt,{},null,[-1,-1,-1])}}export{Ht as component};
