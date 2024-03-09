/**
 * @name SyncTelegram
 * @description Простой плагин 
 * @author 
 * @authorId 
 * @website https://totor13x.com
 * @version 0.0.1
 * @authorLink https://totor13x.com
*/

export default class SyncTelegram {
    url = new URL('https://yourdomain.com/set_status')

    constructor() {
        const token = 'if_you_have_token_you_can_use_it_here'
        const status = 'default'

        this.url.searchParams.set('status', status)
        if (token) {
            this.url.searchParams.set('token', token)
        }

    }
    async updateQuery(status = 'default') {
        this.url.searchParams.set('status', status)

        const response = await BdApi.Net.fetch(this.url.href, {
            method: 'POST'
        })

        return response
    }
    
    async changeStatus(e) {
        if (e.games.length > 0) {
            const game = e.games[0]
            if (game.name.includes('dota 2')) {
                this.updateQuery('dota')
            }
        } else {
            this.updateQuery()
        }
    }

    async start() {
        BdApi.findModuleByProps('subscribe', '_subscriptions').subscribe('RUNNING_GAMES_CHANGE', (e) => this.changeStatus(e))
    }
    stop() {
        BdApi.findModuleByProps('subscribe', '_subscriptions').unsubscribe('RUNNING_GAMES_CHANGE', (e) => this.changeStatus(e))

    }
}