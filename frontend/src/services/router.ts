import { createWebHistory, createRouter } from "vue-router";

import NotFound from "@/pages/notFound.vue";
import Home from "@/pages/home.vue";
import Map from "@/pages/map.vue";
import Portal from "@/pages/portal.vue";
import Status from "@/pages/status.vue";
import Request from "@/pages/request.vue";
import Create from "@/pages/create.vue";

const routes = [
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFound
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/map",
    name: "Map",
    component: Map,
  },
  {
    path: "/portal",
    name: "Portal",
    component: Portal,
  },
  {
    path: "/status",
    name: "Status",
    component: Status,
  },
  {
    path: "/request",
    name: "Request",
    component: Request,
  },
  {
    path: "/create",
    name: "Create",
    component: Create,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
