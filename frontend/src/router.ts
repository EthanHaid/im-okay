import { createWebHistory, createRouter } from "vue-router";

import NotFound from "@/pages/notFound.vue";
import Home from "@/pages/home.vue";
import Map from "@/pages/map.vue";

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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;