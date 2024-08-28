/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'as2.ftcdn.net',
        port: '',
        pathname: '/v2/jpg/02/98/28/57/**',
      },
    ],
  },};


export default nextConfig;

