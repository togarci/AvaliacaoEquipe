import Principal from '@/pages/Principal.vue';

const routes = [
    {
        name: 'Menu',
        path: '/home',        
        component: Principal,
        children: [
            {
                path: '/home',
                name: 'home',
                component: () => import('@/pages/Home.vue')
            },
            {
                path: '/form',
                name: 'formulario',
                component: () => import('@/pages/Form.vue')
            },
            {
                path: '/validacao',
                name: 'validacao',
                component: () => import('@/pages/Validation.vue')
            }
        ]
    },
    {
        path: '/',
        name: 'root',
        redirect: '/login'
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('@/pages/Login.vue')
    },
]

export default routes;
